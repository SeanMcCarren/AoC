with open("2024/1_input.txt", "r") as f:
    input_lines = f.readlines()

tokenized = [l.split("   ") for l in input_lines]
a = sorted([int(token[0]) for token in tokenized])
b = sorted([int(token[1]) for token in tokenized])

c = sum(abs(i - j) for i, j in zip(a, b))

print(c)
