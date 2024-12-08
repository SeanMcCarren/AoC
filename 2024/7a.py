with open("2024/7_input.txt", "r") as f:
    inp = f.readlines()

# inp = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20""".split("\n")


# 292: (((11 6) 16) 20)
def can_form(obj, factors):
    # print("obj", obj, "factors", factors)
    res = False
    if obj < 0:
        res = False
    elif len(factors) == 0:
        res = obj == 0
    elif len(factors) == 1:
        res = factors[0] == obj
    elif len(factors) > 1:
        this_factor = factors[-1]
        new_factors = factors.copy()
        new_factors.pop(-1)
        res = can_form(obj - this_factor, new_factors) or (
            (obj % this_factor == 0) and can_form(round(obj / this_factor), new_factors)
        )

    # print("obj", obj, "factors", factors, "res", res)
    return res


c = 0
for line in inp:
    objective, factors = line.strip("\n").split(": ")
    objective = int(objective)
    factors = [int(f) for f in factors.split(" ")]
    if can_form(objective, factors):
        c += objective

print(c)
