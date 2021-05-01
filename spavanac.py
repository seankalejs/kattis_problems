currenth, currentm = input().split()

beforem = int(currentm) - 45

beforeh = int(currenth)

if beforem < 0:
    beforem += 60
    beforeh -= 1

if beforeh < 0:
    beforeh += 24

print(beforeh, beforem)
