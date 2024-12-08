opp = "ABC"
own = "XYZ"

with open("2024/input") as input:
    t = 0
    for line in input.readlines():
        line = line.strip("\n")
        a = opp.index(line[0])

        b = own.index(line[2])

        win = (b - a + 1) % 3
        score = win * 3 + b + 1
        print(score)
        t += score

    print(t)
