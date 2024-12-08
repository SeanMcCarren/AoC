with open("2024/3_input.txt", "r") as f:
    input_lines = f.read()

import re

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_lines)

s = sum(int(m[0]) * int(m[1]) for m in matches)

print(s)
