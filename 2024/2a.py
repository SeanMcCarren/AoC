with open("2_input.txt", "r") as f:
    input_lines = f.readlines()

def is_safe(lst):
    if len(lst) <= 1:
        return True
    
    if lst[0] == lst[1]:
        return False
    
    inc = lst[0] < lst[1]

    for i in range(len(lst) - 1):
        d = lst[i+1] - lst[i]

        if d == 0 or abs(d) > 3:
            return False

        if inc and d < 0:
            return False
        if not inc and d > 0:
            return False
        
    return True

safes = 0
for line in input_lines:
    if is_safe([int(item) for item in line.split()]):
        safes+=1

print(safes)