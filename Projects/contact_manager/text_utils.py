import os

def center_text(text):
    size = os.get_terminal_size()
    width = int((size[0] - len(text)) / 2)
    print(" " * width, text)

def lower_text(dict: dict, title: str = ""):
    size = os.get_terminal_size()
    height = int((size[1] - len(dict)) - 3)
    if title != '':
        height -= 1
    while height > 0:
        print(" ")
        height -= 1
    if title != '':
        print(title)
    for item in dict:
        print(f"{item}. {dict[item]}")
