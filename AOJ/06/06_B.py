cards = [[False for i in range(13)] for j in range(4)]  # 横縦13*4のリストを作る
pattern = ["S", "H", "C", "D"]

n = int(input())
for i in range(n):  # n回まで繰り返す
    ch, rank = map(str, input().split())
    rank = int(rank)
    cards[pattern.index(ch)][rank - 1] = False  # 指定された要素をFalseからTrueにする
for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j + 1)
