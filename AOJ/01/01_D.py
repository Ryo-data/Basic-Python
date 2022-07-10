S = int(input())
s = S % 60
m = (S // 60) % 60
h = (S // 3600) % 24
print(str(h) + ":" + str(m)+ ":" + str(s))