with open("2024/3_input.txt", "r") as f:
    input_lines = f.read()

import re

matches = re.findall(r"(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))", input_lines)

s = 0

do = True
for m in matches:
    is_do = m[0] != ""
    is_dont = m[1] != ""
    is_mul = m[2] != ""

    assert is_do + is_dont + is_mul == 1

    if is_do:
        do = True
    elif is_dont:
        do = False
    elif is_mul:
        if do:
            s += int(m[3]) * int(m[4])

print(s)
