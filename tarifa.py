limit = int(input())
months = int(input())

sum = 0

for i in range(months):
    cm = int(input())
    sum += limit - cm

print(sum+limit)
