#!/usr/bin/env python3
import numpy as np
import pandas as pd


NUM_SCALE = {chr(x): (idx % 9) + 1 for idx, x in enumerate(range(65, 91))}
EARTHLY_MASTER_NUM = [11, 22, 33]
VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = [chr(x) for x in range(65, 91) if chr(x) not in VOWELS]


def sum_of_letters(name, only_vowels=False, only_consonants=False):
    """SUM OF LETTERS IN NAME"""
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


def final_root(num_list):
    """Single digit"""
    temp_res = sum(num_list)
    if len(str(temp_res)) < 2:
        return sum(num_list)
    else:
        return f"{temp_res} / {reduced_num(temp_res)}"


def num_composition(num_list, name_parts):
    """Helper for pretty printing"""
    for i in range(len(num_list)):
        # breakpoint()
        pad = len(name_parts[i])
        print(f"{num_list[i]:^{pad}}", end=" ")


def original_expressive_key(name):
    """
    ORIGINAL EXPRESSIVE KEY (OEK)
    indicates goals here on earth and provides the necessary]
    guidance for their attainment

    Parameter
    ---------
    name: str, full name of the person

    """
    names = name_split(name.upper())
    name_parts = [v for v in names.values()]
    root_1 = []
    for k, v in names.items():
        res_num = [NUM_SCALE[x] for x in v]
        letters_total = sum(res_num)
        root_1.append(letters_total)

    root_2 = [reduced_num(n) for n in root_1]
    root_3 = [reduced_num(n, emn=False) for n in root_2]
    f_root = final_root(root_3)

    title = "*** Original Expressive Key (OEK) ***"
    dashes = len(title) * "="

    print(f"\n{title}\n{dashes}")
    print(*name_parts)
    num_composition(root_1, name_parts)
    print()
    num_composition(root_2, name_parts)
    print()
    num_composition(root_3, name_parts)
    print()
    print(f"{f_root:^{len(name) - len(names) -1}}")
    # for i in range(len(root_1)):
    #     # breakpoint()
    #     pad = len(name_parts[i])
    #     print(f"{root_1[i]:^{pad}}", end=" ")
    print(f"\n{dashes}")


def gnothology_chart(name):
    """Gnothology Chart - pandas dataframe"""
    nname, osp = original_soul_print(name)
    res_dict = {"name": nname, "osp_1R": osp}
    df = pd.DataFrame.from_dict(res_dict)
    print(df)


if __name__ == '__main__':
    name = "Arun Kumar khatri"
    original_soul_print(name)
