from copy import deepcopy

with open("2024/6_input.txt", "r") as f:
    g = f.readlines()

# g = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".split("\n")


def pp(b):
    for row in b:
        print("".join(row))


g = [list(row) for row in g]
pp(g)

for i, r in enumerate(g):
    if "\n" in r:
        # print(r)
        r.pop(-1)
    assert len(r) == len(g[0])
    assert "\n" not in r

X = len(g[0])
Y = len(g)


def find_start():
    for y, row in enumerate(g):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)


def is_on_screen(x, y):
    return 0 <= x < X and 0 <= y < Y


def is_wall(b, x, y):
    return b[y][x] == "#"


def is_empty(b, x, y):
    return b[y][x] == "." or b[y][x] == "X"


start = find_start()


dx, dy = 0, -1

g[start[1]][start[0]] = "."


def solve(bc):
    x, y = start

    b = deepcopy(bc)

    b[y][x] = "X"

    dx, dy = 0, -1

    history = set([create_unique_history(x, y, dx, dy)])

    while is_on_screen(x + dx, y + dy):
        if is_empty(b, x + dx, y + dy):
            x += dx
            y += dy
            b[y][x] = "X"
        elif is_wall(b, x + dx, y + dy):
            dx, dy = -dy, dx

        if create_unique_history(x, y, dx, dy) in history:
            break

        history.add(create_unique_history(x, y, dx, dy))

    return b


def create_unique_history(hx, hy, hdx, hdy):
    return hx + hy * 10000 + hdx * 100000000 + hdy * 100000000000


def has_loop(start, b):
    x, y = start
    dx, dy = 0, -1

    history = set([create_unique_history(x, y, dx, dy)])

    while is_on_screen(x + dx, y + dy):
        if is_empty(b, x + dx, y + dy):
            x += dx
            y += dy
        elif is_wall(b, x + dx, y + dy):
            dx, dy = -dy, dx
        else:
            print("ERROR '" + g[y + dy][x + dx] + "'")
            print(
                g[y + dy - 1][x + dx - 1]
                + g[y + dy - 1][x + dx]
                + g[y + dy - 1][x + dx + 1]
            )
            print(g[y + dy][x + dx - 1] + g[y + dy][x + dx] + g[y + dy][x + dx + 1])
            print(
                g[y + dy + 1][x + dx - 1]
                + g[y + dy + 1][x + dx]
                + g[y + dy + 1][x + dx + 1]
            )

        if create_unique_history(x, y, dx, dy) in history:
            return True

        history.add(create_unique_history(x, y, dx, dy))
    return False


solved = solve(g)

c = 0
for x in range(X):
    for y in range(Y):
        if (x * Y + y) % 1000 == 0:
            print(f"At row {x}/{X} and column {y}/{Y}")
        if solved[y][x] != "X":
            continue
        if (x, y) == start:
            continue
        if g[y][x] == ".":
            g[y][x] = "#"
            if has_loop(start, g):
                # print("FOUND ONE:")
                # g[y][x] = "O"
                # pp(g)
                # g[y][x] = "#"
                # print("Then the route looks like")
                # pp(solve(g))
                c += 1
            g[y][x] = "."

print(c)
