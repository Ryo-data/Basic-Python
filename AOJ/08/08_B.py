while True:
    x = str(input())
    if x == "0":
        break
    sum = 0
    for d in x:
        sum += int(d)
    print(sum)
