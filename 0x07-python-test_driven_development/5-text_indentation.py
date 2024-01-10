#!/usr/bin/python3
def text_indentation(text):
    """Indents text

    Args:
        text (str): text to indebt

    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    while a < len(text):
        if text[a] in [".", "?", ":"]:
            print(text[a], end="")
            if a + 1 < len(text) and text[a + 1] == ' ':
                print("\n")
                a += 2
                continue
            else:
                print("\n")
        else:
            print(text[a], end="")
        a += 1
