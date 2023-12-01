TO_EXTRACT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_first_char(line, chars) -> str:
    for char in line:
        if char in chars:
            return char
    return ""


def get_last_char(line, chars) -> str:
    for char in reversed(line):
        if char in chars:
            return char
    return ""


def get_combo(line, chars=TO_EXTRACT, type=int):
    return type(get_first_char(line, chars) + get_last_char(line, chars))
