#!/usr/bin/env python3
import numpy as np
import pandas as pd


NUM_SCALE = {chr(x): (idx % 9) + 1 for idx, x in enumerate(range(65, 91))}
EARTHLY_MASTER_NUM = [11, 22, 33]
VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = [chr(x) for x in range(65, 91) if chr(x) not in VOWELS]


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


def num_composition(num_list, name_parts, verbose=True):
    """Helper for pretty printing"""
    if verbose:
        for i in range(len(num_list)):
            # breakpoint()
            pad = len(name_parts[i])
            print(f"{num_list[i]:^{pad}}", end=" ")


def print_and_return(title, name_parts, root_l, verbose=True):
    """
    Print and Return

    Parameter
    ---------
    title: str, name of the procedure;
    name_parts: list of str, part of names splitted;
    root_l: list
    """
    if verbose:
        dashes = len(title) * "-"

        print(f"\n{dashes}\n{title}\n{dashes}")
        print(*name_parts)
        num_composition(root_l, name_parts, verbose=verbose)
        print()

    nl = root_l
    cond = False
    while not cond:
        nl = [reduced_num(n) for n in nl]
        if verbose:
            num_composition(nl, name_parts, verbose=verbose)
            print()

        cond = check_single_digit(nl)

    res, mes = final_root(nl)
    if verbose:
        print(f"{mes:^{len(name) - len(name_parts)}}")
    return res


def original_soul_print(name, verbose=True):
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
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def original_expressive_key(name, verbose=True):
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
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def original_personal_vibration(name, verbose=True):
    """
    ORIGINAL PERSONAL VIBRATION (OPV)
    both good and bad points in outward personality;
    with understanding, can be balanced by OPV

    Parameter
    ---------
    name: str, full name of the person

    """
    name_parts = name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v if x in CONSONANTS]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Original Personal Vibration (OSP) *"
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def change_soul_print(new_name, verbose=True):
    """
    CHANGE SOUL PRINT (CSP)
    add together the total numbers of all VOWELS
    in the new name
    """
    name_parts = new_name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v if x in VOWELS]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Change Soul print (CSP) *"
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def change_personality_vibration(new_name, verbose=True):
    """
    CHANGE PERSONALITY VIBRATION (CPV)
    add together the total numbers of all CONSONANTS
    in the new name
    """
    name_parts = new_name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v if x in CONSONANTS]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Change Personality Vibration (CPV) *"
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def change_expressive_key(new_name, verbose=True):
    """
    CHANGE EXPRESSIVE KEY (CEK)
    Add together the total numbers of every letter.
    """
    name_parts = new_name.upper().split()
    root_1 = []
    for _, v in enumerate(name_parts):
        res_num = [NUM_SCALE[x] for x in v]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    title = "* Change Expressive Key (CEK) *"
    return print_and_return(title, name_parts, root_1, verbose=verbose)


def gnothology_chart(name, new_name, verbose=False):
    """Gnothology Chart - pandas dataframe"""
    osp = original_soul_print(name, verbose=verbose)
    oek = original_expressive_key(name, verbose=verbose)
    opv = original_personal_vibration(name, verbose=verbose)
    csp = change_soul_print(new_name, verbose=verbose)
    cpv = change_personality_vibration(new_name, verbose=verbose)
    cek = change_expressive_key(new_name, verbose=verbose)
    data_dict = {
        'procedure': ['OSP', 'OPV', 'OEK', 'CSP', 'CPV', 'CEK'],
        'value': [osp, opv, oek, csp, cpv, cek]
    }
    df = pd.DataFrame(data_dict)
    title = "* Analysis Summary *"
    dashes = len(title) * "-"

    print(f"\n{dashes}\n{title}\n{dashes}")
    print(df)


if __name__ == '__main__':
    name = "Aarush Arora Khattri"
    new_name = "Aarush A Khattri"
    gnothology_chart(name, new_name)
