with open("2024/9_input", "r") as f:
    inp = f.read().strip("\n")

inp = "2333133121414131402"

print("Opened file")

l = []

def pp(l):
    a = []
    for i in l:
        if i is not None:
            a.append(str(i))
        else:
            a.append(".")
    print("".join(a))

is_empty_space = False
num = 0
for i in inp:
    if is_empty_space:
        for x in range(int(i)):
            l.append(None)
    else:
        for x in range(int(i)):
            l.append(num)
        num += 1

    is_empty_space = not is_empty_space

print(f"Read input: {len(l)} characters")

pp(l)

l2 = []

start_p = 0
end_p = len(l)

while l:
    if len(l) % 1000 == 0:
        print(len(l))
    front = l.pop(0)
    if None is front:
        if l:
            back = l.pop(-1)
            if None is not back:
                l2.append(back)
    else:
        l2.append(front)

pp(l2)

result = sum(idx * item for idx, item in enumerate(l2))

print(result)