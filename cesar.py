
from typing import Tuple

import string as s
import enchant

# Buscar diccionarios en carpeta de instalacion
dict = enchant.Dict("es_CO")


def parse_int(value: str, default: int) -> Tuple[int, bool]:
    """Given a string, parse it into a integer. In case the string dosen't contains any number, returns a default value.

    Args:
        value (str): string to parse
        default (int): default value to return

    Returns:
        Tuple[int, bool]: Fisrt, the parse number or the default value. Second, True if the string has a number, false otherwise.
    """
    try:
        return int(value), True
    except ValueError:
        return default, False


def abc_complete(abc: list):
    complex_abc = s.printable
    for i in range(94):
        abc.append(complex_abc[i])
    abc.append('¿')
    abc.append('á')
    abc.append('é')
    abc.append('í')
    abc.append('ó')
    abc.append('ú')
    return abc


def is_in_list(vect: list, element: int):
    for i in vect:
        if (i == element):
            return True
    return False


def get_may(vect: list):
    may = 0
    for i in vect:
        if (may < i):
            print(f'{may}-{i}')
            may = i
    return vect.index(may)


def d(letter: str, num: int):
    abc = []
    abc = abc_complete(abc)
    pos = abc.index(letter)
    while (num > 0):
        pos -= 1
        if(pos < 0):
            pos = len(abc)-1
        num -= 1
    return abc[pos]


def next_chr(letter: str, delta: int):
    abc = []
    abc = abc_complete(abc)
    pos = abc.index(letter)

    for i in range(1, delta+1):
        pos = pos + 1
        if(pos >= len(abc)):
            pos = 0

    return abc[pos]


def past_chr(letter: str, delta: int):
    abc = []
    abc = abc_complete(abc)
    pos = abc.index(letter)
    while (delta > 0):
        pos = pos - 1
        if (pos < 0):
            pos = len(abc)-1
        delta -= 1

    return abc[pos]


def encode_inv(text: str) -> str:

    encode_text: str = ""

    if (len(text) == 0):
        return ""

    text = text.split(" ")

    delta, sw = parse_int(text[0], 1)  # get the number

    if (len(text) == 1 or not sw):
        start = 0
    else:
        start = 1

    for word in text[start:]:
        for letter in word:
            encode_text += past_chr(letter, delta)

        encode_text += " "

    return encode_text


def encode(text: str) -> str:
    """Given a string, return and encode string

    Args:
        text (str): text to encode

    Returns:
        str: encode text
    """
    encode_text: str = ""

    if (len(text) == 0):
        return ""

    text = text.split(" ")

    delta, sw = parse_int(text[0], 1)  # get the number

    if (len(text) == 1 or not sw):
        start = 0
    else:
        start = 1

    for word in text[start:]:
        for letter in word:
            encode_text += next_chr(letter, delta)

        encode_text += " "

    return encode_text


def decode(text: str) -> str:
    """Given a encode string with a unkown number of shifts, return the decode string.

    Args:
      text (str): encode string

    Returns:
      str: decode string
    """
    abc = []
    abc = abc_complete(abc)
    word = text.split(' ')
    print(word)

    possible_desp = []  # list to save the possible number of n
    # list to cont how many words have a spanish meaning or are aceptable on spanish dict.
    possible_contDesp = []

    for n in range(1, len(abc)):
        for i in (word):
            w = ''
            for j in range(0, len(i)):
                w += d(i[j], n)
            if (dict.check(w)):
                if (not is_in_list(possible_desp, n)):
                    possible_desp.append(n)
                    possible_contDesp.append(1)
                else:
                    pos = possible_desp.index(n)
                    possible_contDesp[pos] += 1
                encode(str(n) + " " + text)
            #print(f'{n} - {i} - {w}')

    print(possible_desp)
    print(possible_contDesp)
    pos = get_may(possible_contDesp)
    n = possible_desp[pos]
    new_text = str(n) + ' '
    for j in range(0, len(word)):
        new_text += word[j] + ' '

    return encode_inv(new_text)
