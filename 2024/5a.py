with open("5_input.txt", "r") as f:
    g = f.read()

a,b = g.split("\n\n")

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

s = 0
for upd in u:
    if len(upd) == 0 or upd[0] == '':
        continue

    if is_update_ok(upd):
        assert len(upd) % 2 == 1

        s += int(upd[len(upd)//2])

print(s)
    

