#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    text = text.strip()
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag is 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')
