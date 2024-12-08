with open("4_input.txt", "r") as f:
    g = f.readlines()

rows = len(g)
cols = len(g[0])

w = "MAS"

def range_check(r, c):
    return (r >= 0 and r < rows and c >= 0 and c < cols)

def count_at(x, y):
    counted = 0
    for dx in (-1, 1):
        for dy in (-1, 1):
            matched = True
            for index, character in enumerate(w):
                offset_index = index - 1
                wx = x + dx * offset_index
                wy = y + dy * offset_index
                if (not range_check(wy, wx) or character != g[wy][wx]):
                    matched = False
                    break
            if matched:
                counted += 1
    assert (counted < 3)

    if counted == 2:
        return 1
    else:
        return 0

total_count = 0
for r in range(rows):
    for c in range(cols):
        total_count += count_at(c, r)

print(total_count)
