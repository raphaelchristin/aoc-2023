import re

RULE = {
    "green": 13,
    "red": 12,
    "blue": 14,
}


def _get_info(line):
    id_re = re.compile("^Game (\\d+):")
    green_re = re.compile("(\\d+) green")
    red_re = re.compile("(\\d+) red")
    blue_re = re.compile("(\\d+) blue")
    id = int(re.match(id_re, line).group(1))
    green = max([int(i) for i in re.findall(green_re, line)])
    blue = max([int(i) for i in re.findall(blue_re, line)])
    red = max([int(i) for i in re.findall(red_re, line)])
    return id, green, blue, red


def get_id_or_zero(line, rule=RULE):
    id, green, blue, red = _get_info(line)
    if green > rule["green"] or blue > rule["blue"] or red > rule["red"]:
        return 0
    return id


def get_power(line):
    _, green, blue, red = _get_info(line)
    return green * blue * red
