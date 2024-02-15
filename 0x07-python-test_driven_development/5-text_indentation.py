#!/usr/bin/python3

def text_indentation(text):
    """prints a text with 2 new lines after each of 
    these characters: ., ? and :

    Args:
        size: is the size length of the square

    Raises: 
        TypeError: text is not string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
