#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Indents given text by adding two new lines after each of
    of these characters: ., ?, and :

    Args:
        text: text to be indented
        type accepted: string

    Raise:
        raises TypeError if text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    space_checker = True
    for char in text:
        if space_checker is True and char == " ":
            continue
        space_checker = False
        print(char, end="")
        if char in ["?", ".", ":"]:
            space_checker = True
            print("\n")
