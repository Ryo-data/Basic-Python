count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
building = 1

n = int(input())
for i in range(n):  # n回まで繰り返す
    b, f, r, v = map(int, input().split())
    count[b - 1][f - 1][r - 1] += v
for c1 in count:
    for c2 in c1:
        for c3 in c2:
            print(" " + str(c3), end="")
        print()
    if building <= 3:
        print("#" * 20)
        building += 1
