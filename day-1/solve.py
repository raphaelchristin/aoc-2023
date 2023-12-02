DIGITS_SPELLED = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGITS_DELLEPS = {key[::-1]: value for key, value in DIGITS_SPELLED.items()}


def get_char(line, allow_spelled=False, spelled=DIGITS_SPELLED) -> str:
    ptr = 0
    while ptr < len(line):
        if line[ptr].isdigit():
            return line[ptr]
        elif allow_spelled:
            for digit, c in spelled.items():
                if digit in line[0 : ptr + 1]:
                    return c
        ptr += 1
    return ""


def get_line_num(line, allow_spelled=False):
    return int(
        get_char(line, allow_spelled)
        + get_char(line[::-1], allow_spelled, DIGITS_DELLEPS)
    )
