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

X = len(g[0])
Y = len(g)


def find_start():
    for y, row in enumerate(g):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)


def is_on_screen(x, y):
    return 0 <= x < X and 0 <= y < Y


def is_wall(x, y):
    return g[y][x] == "#"


def is_empty(x, y):
    return g[y][x] == "." or g[y][x] == "X"


start = find_start()

x, y = start

g[y][x] = "X"

dx, dy = 0, -1

while is_on_screen(x + dx, y + dy):
    if is_empty(x + dx, y + dy):
        x += dx
        y += dy
        g[y][x] = "X"
    elif is_wall(x + dx, y + dy):
        dx, dy = -dy, dx

pp(g)

s = sum(sum(1 for cell in row if cell == "X") for row in g)

print(s)
