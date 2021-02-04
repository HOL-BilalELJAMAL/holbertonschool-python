#!/usr/bin/python3
"""
    5-text_indentation.py
    Module that defines a method for printing a text with
    2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that takes a text as string and prints a text with
    2 new lines after each of these characters: ., ? and :

    Args:
        text (str): Text

    Note:
        If text is not a string, a TypeError exception is raised
        Otherwise, prints a text with 2 new lines after mentioned characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cnt, cnt1, cnt2 = 0, 0, 0
    org_str = text
    rev_str = org_str[::-1]
    str_size = len(org_str)
    if text[str_size - 1] == ' ':
        for char in rev_str:
            if char == ' ' and cnt2 == 0:
                cnt1 += 1
            if char != ' ':
                cnt2 = 1
        org_str = rev_str[cnt1:str_size][::-1]
    for char in org_str:
        if not char == ' ' or not cnt == 0:
            print(char, end="")
            cnt = 1
        if char == '.' or char == '?' or char == ':':
            print("\n")
            cnt = 0
