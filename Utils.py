# -*- coding: utf-8 -*-
"""
Created on Sat Jun 5 15:30:03 2021
@author: ryanz
"""

CHAR_MAP = {
    "Λ": 'A',
    "λ": 'A',
    "ß": "B",
    "¢": "c",
    "Ξ": "E",
    "σ": "o", 
    "や": "P",
    "$": "S",
    "ν": "v", 
    "γ": "y"
}

VALID_CHARS = "/\*^+-abcdefghijklmnopqrstuvwxyz\u03A9\u038F" + "abcdefghijklmnopqrstuvwxyz0123456789".upper()

PRE_REMOVE = "/\*^+-"


def is_CJK(char):
    return any([start <= ord(char) <= end for start, end in 
                [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), 
                 (63744, 64255), (65072, 65103), (65381, 65500), 
                 (131072, 196607)]
                ])

from unidecode import unidecode

def sanitize_uni(string):
    '''
    convert known/common un-unidecodable strings to unicode, then strip all non-
    Returns
    -------
    string with no CJK and non-unicode characters
    '''
    
    string = [CHAR_MAP.get(i, i) for i in string]
    ret = list(unidecode(''.join(string)))
    while len(ret)>0:
        if ret[0] in PRE_REMOVE or ret[0] not in VALID_CHARS:
            ret.pop(0)
        else:
            break
    return ''.join(ret)


def sanitize_tag_uni(string):
    '''
    get rid of non-unicode characters that cannot be converted, but keep convertable characters in original form
    '''
    string = [i for i in string if CHAR_MAP.get(i, i) in VALID_CHARS or (unidecode(i)!="" and unidecode(i) in VALID_CHARS)]
    while len(string)>0:
        if string[0] in PRE_REMOVE:
            string.pop(0)
        else:
            break
    return ''.join(string)

def replace_brackets(string):
    string = string.lstrip('[').lstrip(']').lstrip('(').lstrip(')').lstrip('{').lstrip('}')
    string = list(unidecode(sanitize_uni(string)))
    ret = [i for i in string if i in VALID_CHARS]
    
    return ''.join(ret)

def dis_clean(string):
    return string.replace("*", "\*").replace("`",'\`').replace("_", "\_").replace("~~", "\~~")


if __name__ == "__main__":
    i = "!A★A"
    print(sanitize_uni(i))
    
    
