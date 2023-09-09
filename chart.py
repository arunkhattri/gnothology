#!/usr/bin/env python3
import numpy as np
import pandas as pd


NUM_SCALE = {chr(x): (idx % 9) + 1 for idx, x in enumerate(range(65, 91))}
EARTHLY_MASTER_NUM = [11, 22, 33]
VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = [chr(x) for x in range(65, 91) if chr(x) not in VOWELS]


def sum_of_letters(name, only_vowels=False, only_consonants=False):
    """SUM OF LETTERS IN NAME"""
    name = name.upper()
    if only_vowels:
        res_name = [letter for letter in name if letter in VOWELS]
    elif only_consonants:
        res_name = [letter for letter in name if letter in CONSONANTS]
    else:
        res_name = name

    res = 0

    for letter in res_name:
        res += NUM_SCALE[letter]
    return res


def name_split(name):
    """Split the name."""
    res = name.split(" ")
    res_dict = dict()
    for idx, elem in enumerate(res):
        res_dict[f"name_{idx + 1}"] = elem
    return res_dict


def reduced_num(num, emn=True):
    """Reduce the int to single digit int"""
    # print(num)
    if len(str(num)) == 1:
        res = num
    elif emn & (num in EARTHLY_MASTER_NUM):
        res = num
    else:
        res = sum([int(x) for x in str(num)])

    return res


def check_single_digit(num_list):
    """Find if all items in list are single digit"""
    digits = [len(str(x)) for x in num_list]
    # return all((i < 2 or i in EARTHLY_MASTER_NUM) for i in digits)
    for i in range(len(digits)):
        if digits[i] > 1 and num_list[i] not in EARTHLY_MASTER_NUM:
            return False
    return True


def final_root(num_list):
    """Single digit"""

    # check if it's a list or int
    res = sum(num_list)

    digits = len(str(res))
    mes = f"{res}"

    if digits < 2 or res in EARTHLY_MASTER_NUM:
        res = res
    else:
        res = reduced_num(res)
        mes += f" / {res}"
        cond = len(str(res)) < 2 or res in EARTHLY_MASTER_NUM
        if not cond:
            res = reduced_num(res)
            mes += f" / {res}"

    return res, mes


def num_composition(num_list, name_parts):
    """Helper for pretty printing"""
    for i in range(len(num_list)):
        # breakpoint()
        pad = len(name_parts[i])
        print(f"{num_list[i]:^{pad}}", end=" ")


def print_and_return(title, name_parts, root_l):
    """
    Print and Return

    Parameter
    ---------
    title: str, name of the procedure;
    name_parts: list of str, part of names splitted;
    root_l: list,
    """
    dashes = len(title) * "-"

    print(f"\n{dashes}\n{title}\n{dashes}")
    print(*name_parts)
    num_composition(root_l, name_parts)
    print()

    nl = root_l
    cond = False
    while not cond:
        nl = [reduced_num(n) for n in nl]
        num_composition(nl, name_parts)
        print()
        cond = check_single_digit(nl)

    res, mes = final_root(nl)
    print(f"{mes:^{len(name) - len(name_parts)}}")
    return res


def original_expressive_key(name):
    """
    ORIGINAL EXPRESSIVE KEY (OEK)
    indicates goals here on earth and provides the necessary]
    guidance for their attainment

    Parameter
    ---------
    name: str, full name of the person

    """
    name_parts = name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Original Expressive Key (OEK) *"
    return print_and_return(title, name_parts, root_1)


def original_soul_print(name):
    """
    ORIGINAL SOUL PRINT (OSP)
    inner soul desire; deepest longings; highest goal;
    dream come true

    Parameter
    ---------
    name: str, full name of the person

    """
    name_parts = name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v if x in VOWELS]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Original Soul print (OSP) *"
    return print_and_return(title, name_parts, root_1)


def gnothology_chart(name):
    """Gnothology Chart - pandas dataframe"""
    pass


if __name__ == '__main__':
    name = "Aaryaansh Arora Khattri"
    osp = original_soul_print(name)
    oek = original_expressive_key(name)
    data_dict = {
        'procedure': ['OSP', 'OEK'],
        'value': [osp, oek]
    }
    df = pd.DataFrame(data_dict)
    title = "* Analysis Summary *"
    dashes = len(title) * "-"

    print(f"\n{dashes}\n{title}\n{dashes}")
    print(df)
