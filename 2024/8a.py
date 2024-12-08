with open("2024/8_input", "r") as f:
    inp = f.readlines()

# inp = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".splitlines()

g = [list(row.strip("\n")) for row in inp]

antennas = {}
for y, row in enumerate(g):
    for x, cell in enumerate(row):
        if cell != ".":
            if cell not in antennas:
                antennas[cell] = [(x, y)]
            else:
                antennas[cell].append((x, y))

X = len(g[0])
Y = len(g)


def is_in_bounds(x, y):
    return 0 <= x < X and 0 <= y < Y


antinodes = set()

for antenna, locations in antennas.items():
    if len(locations) > 1:
        for loc1 in locations:
            for loc2 in locations:
                if loc1 == loc2:
                    antinodes.add(loc1)
                    continue
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                x = loc2[0] + dx
                y = loc2[1] + dy
                while is_in_bounds(x, y):
                    antinodes.add((x, y))
                    x += dx
                    y += dy

print(len(antinodes))
