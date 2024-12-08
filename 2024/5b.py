from collections import deque

with open("2024/5_input.txt", "r") as f:
    g = f.read()


a, b = g.split("\n\n")

r = [item.split("|") for item in a.split("\n")]

u = [item.split(",") for item in b.split("\n")]


def is_update_ok(update):
    for index, item in enumerate(update):
        for rule in r:
            if rule[0] == item:
                for past_item_in_update in update[:index]:
                    if past_item_in_update == rule[1]:
                        return False
    return True


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def reorder_upd(update):
    nodes = {item: Node(item) for item in update}

    for rule in r:
        if rule[0] in nodes and rule[1] in nodes:
            nodes[rule[0]].add_child(nodes[rule[1]])
            nodes[rule[1]].add_parent(nodes[rule[0]])

    in_degree = {node: len(nodes[node].parents) for node in nodes}
    queue = deque([node for node in nodes if in_degree[node] == 0])
    reordered_upd = []

    while queue:
        current = queue.popleft()
        reordered_upd.append(current)

        for child in nodes[current].children:
            in_degree[child.name] -= 1
            if in_degree[child.name] == 0:
                queue.append(child.name)

    assert len(reordered_upd) == len(update)

    return reordered_upd


s = 0
for upd in u:
    if len(upd) == 0 or upd[0] == "":
        continue

    if not is_update_ok(upd):
        reordered_upd = reorder_upd(upd)

        assert len(reordered_upd) % 2 == 1

        s += int(reordered_upd[len(reordered_upd) // 2])

print(s)
