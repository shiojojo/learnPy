c0 = int(input("c0:"))
steps = 0

while c0 != 1:
    steps += 1
    if c0 % 2:
        c0 = c0 * 3 + 1
        print(c0)
    else:
        c0 = c0 // 2
        print(c0)

print("steps = " + str(steps))