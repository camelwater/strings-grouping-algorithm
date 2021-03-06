from itertools import chain
from functools import reduce, partial
from collections import deque
from typing import List

def ngram(seq: str, n: int):
    return (seq[i: i+n] for i in range(0, len(seq)-n+1))

def allngram(seq: str, minn=1, maxn=None):
    lengths = range(minn, maxn+1) if maxn else range(minn, len(seq))
    ngrams = map(partial(ngram, seq), lengths)
    return set(chain.from_iterable(ngrams))

def commonaffix(group):
    maxn = min(map(len, group))
    seqs_ngrams = map(partial(allngram, maxn=maxn), group)
    intersection = reduce(set.intersection, seqs_ngrams)
    try:
        all_presub = sorted(intersection, key=len, reverse=True)
        for sub in all_presub:
            if all([i.startswith(sub) or i.endswith(sub) for i in group]):
                return sub

        return ""
    except:
        return ""

def common_actual_affix(player: str, comp: str):
    # longest_match = 0
    for temp_indx in range(len(min(player, comp, key=len)), 0, -1):
        if player[:temp_indx] == comp[:temp_indx] or player[:temp_indx] == comp[-temp_indx:]:
            # match = len(player[:temp_indx].strip())
            # if match>0: return True
            return True

        if player[-temp_indx:] == comp[-temp_indx:] or player[-temp_indx:] == comp[:temp_indx]:
            # match = len(player[:temp_indx].strip())
            # if match>0: return True
            return True
    return False

def is_CJK(char) -> bool:
    return any([start <= ord(char) <= end for start, end in 
                [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), 
                 (63744, 64255), (65072, 65103), (65381, 65500), 
                 (131072, 196607)]
                ])

from unidecode import unidecode

def sanitize_uni(string: str, for_search = False):
    '''
    convert known/common un-unidecodable and unicode strings to ASCII and clean string for tag-matching

    '''  
    ret = []
    for i in string:
        if i in MULT_CHAR_MAP:
            for char in MULT_CHAR_MAP[i]:
                ret.append(char)
            continue
        i = CHAR_MAP.get(i, i)
        if i in VALID_CHARS or is_CJK(i):
            ret.append(i)
        else:
            ret.append(" ")
       
       
    if for_search:
        return ''.join(ret)

    remove = True
    while remove and len(ret)>0:
        remove = False
        if ret[0] in PRE_REMOVE:
            ret.pop(0)
            remove = True
        if len(ret)>0 and ret[-1] in POST_REMOVE:
            ret.pop()
            remove = True

    return ''.join(ret)


def sanitize_tag_uni(string):
    '''
    get rid of non-unicode characters that cannot be converted, but keep convertable characters in original form
    '''
    string = [i for i in string if CHAR_MAP.get(i, i) in VALID_CHARS or is_CJK(i) or i in MULT_CHAR_MAP or (unidecode(i)!="" and unidecode(i) in VALID_CHARS)]
    while len(string)>0:
        if string[0] in PRE_REMOVE:
            string.pop(0)
        elif string[-1] in POST_REMOVE:
            string.pop(-1)
        else:
            break

    return ''.join(string)


# CONSTANTS

VALID_CHARS = set("/\*`^+-_.!?@%&()\u03A9\u038F" + "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz0123456789 ".upper())
PRE_REMOVE = set("/\*^+-_.!?#%() ")
POST_REMOVE = set("/\*^+-.!?# ")

CHAR_MAP = {
    "??": 'A', "??": 'A', "@": 'A', "??": "A", "??": "A", "??": "A", "??": "A", "??": "A", "??": "A", "??": "A", "??": "A", "??": "a", "??": "a", "??": "a", "??": "a", "??": "a", "??": "a", "??": "a", "??": "a", "??": "a",
    
    "???": "b", "??": "B", "??": "B",
    
    "??": "c", "??": "c", "??": "c", "??": "c", "??": "C",
    
    "??": "e", "??": "e", "??": "e", "??": "e", "??": "e", "???": "e", "??": "E", "???": "E", "??": "E", "??": "E", "??": "E", "??": "E", "??": "E", "??": "E", "??": "E", "??": "E", "??": "E",
    
    "??": "H",

    "??": "i", "??": "i", "??": "i", "??": "i", "??": "i", "??": "i", "??": "i", "??": "i", "??": "I", "??": "I", "??": "I", "??": "I", "??": "I", "??": "I",
    
    "??": "k", 

    "??": "n", "??": "n", "??": "n", "??": "N", "??": "N",

    "??": "o", "???": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "o", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "??": "O", "???": "O",
    
    "???": "P", "??": "p",
    
    "??": "r", "??": "r", "??": "R",
    
    "$": "S", "??": "S",
    
    "??": "t",
    
    "??": "u", "??": "u", "??": "u", "??": "u", "??": "u", "??": "u", "??": "u", "??": "U", "??": "U", "??": "U", "??": "U", "??": "U", "??": "u",
    
    "??": "v",

    "??": "w", "??": "w", "??": "w", "??": "W",
    
    "??": "X",
    
    "??": "y", "??": "y", "??": "y", "??": "Y", "??": "Y", "??": "Y", "??": "Y", "??": "Y",
    
    "??": "Z", "??": "Z",

    "???": "[", "???": "]", "???": "[", "???": "]"
}

MULT_CHAR_MAP = {
    "??": 'AE',
    "??": "ae",

    "??": "oe",
    "??": "OE",

    "???": "TM"
}
