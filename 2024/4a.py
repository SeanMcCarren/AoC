with open("4_input.txt", "r") as f:
    g = f.readlines()

rows = len(g)
cols = len(g[0])

w = "XMAS"

def range_check(r, c):
    return (r >= 0 and r < rows and c >= 0 and c < cols)

def count_at(x, y):
    counted = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            matched = True
            for index, character in enumerate(w):
                wx = x + dx * index
                wy = y + dy * index
                if (not range_check(wy, wx) or character != g[wy][wx]):
                    matched = False
                    break
            if matched:
                counted += 1
    # if counted:
    #     print(f"counted {counted} at {x}, {y}")
    return counted

total_count = 0
for r in range(rows):
    for c in range(cols):
        total_count += count_at(c, r)

print(total_count)
