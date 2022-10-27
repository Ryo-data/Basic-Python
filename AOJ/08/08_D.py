s = str(input())
s += s  # 2周すれば最後と最初の文字をつながることができる
p = str(input())
if s.find(p) != -1:  # sの中にpがあればTrueを返す
    print("Yes")
else:
    print("No")
