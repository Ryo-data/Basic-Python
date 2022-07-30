count = 0
a, b, c = map(int, input().split())
for num in range(a, b + 1):
    if c % num == 0:
        count = count + 1
print(count)
