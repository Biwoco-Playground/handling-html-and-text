


def map_language(language_code):
    if language_code == None:
        return None
    return languageMap[language_code.lower()]


def get_stoplist(language):
    return set(
                line.strip() for line in open('stoplists/' + language + '.txt'))


languageMap = {
    "vietnamese": "Vietnamese",
    "vn": "Vietnamese",
    "vn-vn": "Vietnamese",
    "vietnam": "Vietnamese",
    "vi": "Vietnamese",

    "english": "English",
    "simple_english": "Simple_English",
    "en": "Simple_English",
    "en-au": "Simple_English",
    "en-bz": "Simple_English",
    "en-ca": "Simple_English",
    "en-ie": "Simple_English",
    "en-jm": "Simple_English",
    "en-nz": "Simple_English",
    "en-ph": "Simple_English",
    "en-za": "Simple_English",
    "en-tt": "Simple_English",
    "en-gb": "Simple_English",
    "en-us": "Simple_English",
    "en-uk": "Simple_English",
    "en-zw": "Simple_English",

    "french": "French",
    "fr": "French",
    "fr-be": "French",
    "fr-ca": "French",
    "fr-fr": "French",
    "fr-lu": "French",
    "fr-mc": "French",
    "fr-ch": "French",

    "dutch": "Dutch",
    "nl": "Dutch",

    "italian": "Italian",
    "it": "Italian",
    "it-ch": "Italian",

    "portuguese": "Portuguese",
    "pt": "Portuguese",
    "pt-br": "Portuguese",
    "pt-pt": "Portuguese",

    "russian": "Russian",
    "ru": "Russian",
    "ru-mo": "Russian",
    "ru-ru": "Russian",

    "spanish": "Spanish",
    "es": "Spanish",
    "es-ar": "Spanish",
    "es-bo": "Spanish",
    "es-cl": "Spanish",
    "es-co": "Spanish",
    "es-cr": "Spanish",
    "es-do": "Spanish",
    "es-ec": "Spanish",
    "es-sv": "Spanish",
    "es-gt": "Spanish",
    "es-hn": "Spanish",
    "es-mx": "Spanish",
    "es-ni": "Spanish",
    "es-pa": "Spanish",
    "es-py": "Spanish",
    "es-pe": "Spanish",
    "es-pr": "Spanish",
    "es-es": "Spanish",
    "es-uy": "Spanish",
    "es-ve": "Spanish",

    "korean": "Korean",
    "ko": "Korean",
    "kr": "Korean",

    "indonesian": "Indonesian",
    "in": "Indonesian",

    "malay": "Malay",

    "afrikaans": "Afrikaans",
    "af": "Afrikaans",

    "albanian": "Albanian",
    "sq": "Albanian",

    "arabic": "Arabic",
    "ar": "Arabic",

    "aragonese": "Aragonese",
    "an": "Aragonese",

    "armenian": "Armenian",
    "hy": "Armenian",

    "aromanian": "Aromanian",

    "asturian": "Asturian",

    "azerbaijani": "Azerbaijani",
    "az": "Azerbaijani",

    "basque": "Basque",
    "eu": "Basque",

    "belarusian": "Belarusian",
    "belarusian_taraskievica": "Belarusian_Taraskievica",

    "bengali": "Bengali",
    "bn": "Bengali",

    "bishnupriya_manipuri": "Bishnupriya_Manipuri",
    "bosnian": "Bosnian",

    "breton": "Breton",
    "br": "Breton",

    "bulgarian": "Bulgarian",
    "bg": "Bulgarian",

    "catalan": "Catalan",
    "ca": "Catalan",

    "cebuano": "Cebuano",
    "chuvash": "Chuvash",

    "croatian": "Croatian",
    "hr": "Croatian",

    "czech": "Czech",
    "cs": "Czech",

    "danish": "Danish",
    "da": "Danish",

    "esperanto": "Esperanto",
    "eo": "Esperanto",

    "estonian": "Estonian",
    "et": "Estonian",

    "finnish": "Finnish",
    "fi": "Finnish",

    "galician": "Galician",
    "gl": "Galician",

    "georgian": "Georgian",
    "ka": "Georgian",

    "german": "German",
    "de": "German",
    "de-at": "German",
    "de-de": "German",
    "de-li": "German",
    "de-lu": "German",
    "de-ch": "German",

    "greek": "Greek",
    "el": "Greek",

    "gujarati": "Gujarati",
    "gu": "Gujarati",

    "haitian": "Haitian",
    "ht": "Haitian",

    "hebrew": "Hebrew",
    "he": "Hebrew",
    "iw": "Hebrew",

    "hindi": "Hindi",
    "hi": "Hindi",

    "hungarian": "Hungarian",
    "hu": "Hungarian",

    "icelandic": "Icelandic",
    "is": "Icelandic",

    "ido": "Ido",
    "io": "Ido",

    "igbo": "Igbo",

    "irish": "Irish",
    "ga": "Irish",

    "kannada": "Kannada",
    "kn": "Kannada",

    "kurdish": "Kurdish",
    "ku": "Kurdish",

    "latin": "Latin",
    "la": "Latin",

    "latvian": "Latvian",
    "lettish": "Latvian",
    "lv": "Latvian",

    "lithuanian": "Lithuanian",
    "lt": "Lithuanian",

    "lombard": "Lombard",
    "low_saxon": "Low_Saxon",
    "luxembourgish": "Luxembourgish",

    "macedonian": "Macedonian",
    "mk": "Macedonian",

    "malayalam": "Malayalam",

    "maltese": "Maltese",
    "mt": "Maltese",

    "marathi": "Marathi",
    "mr": "Marathi",

    "neapolitan": "Neapolitan",

    "nepali": "Nepali",
    "ne": "Nepali",

    "newar": "Newar",

    "norwegian_bokmal": "Norwegian_Bokmal",
    "no-bo": "Norwegian_Bokmal",
    "no": "Norwegian_Bokmal",
    "nob": "Norwegian_Bokmal",
    "nb": "Norwegian_Bokmal",
    "norwegian_nynorsk": "Norwegian_Nynorsk",
    "no-ny": "Norwegian_Nynorsk",
    "nno": "Norwegian_Nynorsk",
    "nn": "Norwegian_Nynorsk",

    "occitan": "Occitan",
    "oc": "Occitan",

    "persian": "Persian",
    "piedmontese": "Piedmontese",

    "polish": "Polish",
    "pl": "Polish",

    "quechua": "Quechua",
    "qu": "Quechua",

    "romanian": "Romanian",
    "ro": "Romanian",

    "samogitian": "Samogitian",

    "serbian": "Serbian",
    "sr": "Serbian",

    "serbo_croatian": "Serbo_Croatian",
    "sicilian": "Sicilian",

    "slovak": "Slovak",
    "sk": "Slovak",

    "slovenian": "Slovenian",
    "sl": "Slovenian",

    "sundanese": "Sundanese",
    "su": "Sundanese",

    "swahili": "Swahili",
    "kiswahili": "Swahili",
    "sw": "Swahili",

    "swedish": "Swedish",
    "sv": "Swedish",

    "tagalog": "Tagalog",
    "tl": "Tagalog",

    "tamil": "Tamil",
    "ta": "Tamil",

    "telugu": "Telugu",
    "te": "Telugu",

    "turkish": "Turkish",
    "tr": "Turkish",

    "ukrainian": "Ukrainian",
    "uk": "Ukrainian",

    "urdu": "Urdu",
    "ur": "Urdu",

    "volapuk": "Volapuk",
    "vo": "Volapuk",

    "walloon": "Walloon",
    "wa": "Walloon",

    "waray_waray": "Waray_Waray",

    "welsh": "Welsh",
    "cy": "Welsh",

    "west_frisian": "West_Frisian",
    "western_panjabi": "Western_Panjabi",

    "yoruba": "Yoruba",
    "yo": "Yoruba",
}