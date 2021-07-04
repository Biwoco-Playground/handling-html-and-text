import stopwords_manager
import utils

from lxml.html.clean import Cleaner
from lxml.html import fromstring
from models import Block
from langdetect import detect


MAX_LINK_DENSITY = 0.2
LENGTH_LOW = 10
LENGTH_HIGH = 30
STOPWORDS_LOW = 0.20
STOPWORDS_HIGH = 0.32
PARAGRAPH_TAGS = [
    'body', 'blockquote', 'caption', 'center', 'col', 'colgroup', 'dd',
    'div', 'dl', 'dt', 'fieldset', 'form', 'legend', 'optgroup', 'option',
    'p', 'pre', 'table', 'td', 'textarea', 'tfoot', 'th', 'thead', 'tr',
    'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
]
TITLE_TAG = 'h1'


def preprocess(str_html):     
    print("Preprocessing...")
    options = {
            "processing_instructions": False,
            "remove_unknown_tags": False,
            "safe_attrs_only": False,
            "page_structure": False,
            "annoying_tags": False,
            "frames": False,
            "meta": False,
            "links": False,
            "javascript": False,
            "scripts": True,
            "comments": True,
            "style": True,
            "embedded": True,
            "forms": True,
            "kill_tags": (
                        "head", "select"
                        "nav", "figure", 
                        "noscript", "footer",
                        "iframe"),}
    
    cleaner = Cleaner(**options)

    return cleaner.clean_html(str_html)


def divide_blocks(str_html):
    print("Dividing html into blocks...")
    blocks = []
    tree = fromstring(str_html)

    tree_text = utils.normalize_whitespace(str(
                                                tree.xpath("//text()")))
    print("Detecting language code...")
    language_code = detect(tree_text)
    print("Language code: " + language_code)
    language = stopwords_manager.map_language(language_code)
    stopwords = stopwords_manager.get_stoplist(language)

    tree_iter = tree.iter()
    flag = False
    for tag in tree_iter:
        current_tag = tag.tag  
        if current_tag == TITLE_TAG:
            flag = True

        if (flag 
            and current_tag in PARAGRAPH_TAGS):
            text = tag.text
            if (text is not None):
                count_stopwords = 0
                content = text.split(" ")
                total_words = len(content)
                for sub in content:
                    if sub in stopwords:
                        count_stopwords += 1
                stopwords_density = count_stopwords/total_words

                count_a = 0
                link_density = 0
                for child in tag:
                    child_text = child.text
                    if (child.tag == 'a' 
                        and child_text is not None):
                        len_child = len(child_text)
                        if (total_words
                            and len_child):
                            count_a += 1
                            link_density += len_child/total_words

                if count_a > 0:
                    link_density /= count_a

                quality = ""
                if current_tag == TITLE_TAG:
                    quality = "good"
                else:
                    quality = classify_block(
                                            link_density, total_words, 
                                            stopwords_density)
                
                block = Block(
                            text, total_words, 
                            stopwords_density, link_density,
                            quality)

                blocks.append(block)
            
    return blocks


def classify_block(
                link_density, length, 
                stopwords_density):
    if link_density > MAX_LINK_DENSITY:
        return 'bad'

    if length < LENGTH_LOW:
        if link_density > 0:
            return 'bad'
        else:
            return 'short'

    if stopwords_density > STOPWORDS_HIGH:
        if length > LENGTH_HIGH:
            return 'good'
        else:
            return 'near-good'
            
    if stopwords_density > STOPWORDS_LOW:
        return 'near-good'
    else:
        return 'bad'


def get_main_content(blocks):
    print("Getting main content...")
    main_content = ""
    index = 0
    for block in blocks:
        block_quality = block.quality
        block.quality = get_context_sensitive_class(
                                                    blocks, block_quality, 
                                                    index)
        if block.quality == 'good':
            main_content += block.content + "\n"

        index += 1

    main_content = utils.normalize_whitespace(main_content)
    return main_content


def get_context_sensitive_class(
                                blocks, block_quality, 
                                index):
    if block_quality == 'bad':
        return 'bad'

    if block_quality == 'good':
        return 'good'

    if block_quality == 'near-good':
        prev_block_quality = get_prev_good_or_bad_block(blocks, index)
        next_block_quality = get_next_good_or_bad_block(blocks, index)
        if prev_block_quality == 'good' or next_block_quality == 'good':
            return 'good'
        else:
            return 'bad'

    if block_quality == 'short':
        prev_block_quality = get_prev_good_or_bad_block(blocks, index)
        next_block_quality = get_next_good_or_bad_block(blocks, index)
        if prev_block_quality == 'bad' and next_block_quality == 'bad':
            return 'bad'

        if prev_block_quality == 'good' and next_block_quality == 'good':
            return 'good'

        if prev_block_quality == 'bad' and next_block_quality == 'good':
            if get_prev_non_short_block(blocks, index) == 'near-good':
                return 'good'
            else:
                return 'bad'

        if next_block_quality == 'bad' and prev_block_quality == 'good':
            if get_next_non_short_block(blocks, index) == 'near-good':
                return 'good'
            else:
                return 'bad'


def get_prev_good_or_bad_block(blocks, index):
    i = index
    while i > 0:
        i -= 1
        block_quality = blocks[i].quality
        if block_quality == 'good':
            return block_quality
    return 'bad'


def get_next_good_or_bad_block(blocks, index):
    i = index
    len_blocks = len(blocks)
    while i < len_blocks - 1:
        i += 1
        block_quality = blocks[i].quality
        if block_quality == 'good':
            return block_quality
    return 'bad'


def get_prev_non_short_block(blocks, index):
    i = index
    while i > 0:
        i -= 1
        block_quality = blocks[i].quality
        if block_quality != 'short':
            return block_quality
    return 'bad'


def get_next_non_short_block(blocks, index):
    i = index
    len_blocks = len(blocks)
    while i < len_blocks - 1:
        i += 1
        block_quality = blocks[i].quality
        if block_quality != 'short':
            return block_quality
    return 'bad'