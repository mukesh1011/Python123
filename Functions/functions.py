def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


print(center_text("spam and eggs"))
print(center_text("spam, spam and eggs"))
print(center_text("spa, spam, spam, and spam"))
print(center_text("first", "second", 3, 4, "spam", sep=":"))


