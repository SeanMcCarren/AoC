with open("2024/input") as input:
    max_total = 0
    total = 0
    for line in input.readlines():
        line = line.strip("\n")
        if line == "":
            max_total = max(total, max_total)
            total = 0
        else:
            total += int(line)
    print(max_total)
