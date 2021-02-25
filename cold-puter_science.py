num = int(input())
sum = 0

t = list(input().split())

for i in range(num):
    if int(t[i]) < 0:
        sum += 1

print(sum)
