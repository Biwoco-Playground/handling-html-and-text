import re
import os

from timeit import default_timer


def init_results_dir():
    print("Initializing results directory...")
    dir = 'results'
    if not os.path.exists(dir):
        os.makedirs(dir)


def clone_page(requests_session, url):
    print("Cloning url: " + url)
    headers = {'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64)'
                +' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
    response = requests_session.get(url, headers = headers)
    print(response)
    return response


def calculate_compiling_time(start_time):
    stop_time = default_timer()
    with open('results/compiling_time.txt', 'w') as compiling_time:
        compiling_time.write(
                            'Compiling time: {time}'.format(
                                                            time = stop_time - start_time))


def dump_file(str_content, filename):
    print("Dumping file: " + filename)
    with open("results/" + filename, "w") as f:
        f.write(str_content)
    print("Your file is results/" + filename)


MULTIPLE_WHITESPACE_PATTERN = re.compile(r"\s+", re.UNICODE)


def normalize_whitespace(text):
    return MULTIPLE_WHITESPACE_PATTERN.sub(replace_whitespace, text)


def replace_whitespace(match):
    text = match.group()
    if "\n" in text or "\r" in text:
        return "\n"
    else:
        return " "