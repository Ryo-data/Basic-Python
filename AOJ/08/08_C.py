import sys

count = [0] * 26

words = sys.stdin.read().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
# sys.studin.readで複数行の文字列を複数行のまま受け取ることができる
# .lowerでアルファベットの大文字を小文字に直す
for m in words:  # wordsの要素を一つずつmに代入
    i = 0  # 毎回iのカウントを0に戻す
    for n in alphabet:  # alphabetの要素を一つずつnに代入
        if m == n:  # mとnのアルファベットが一致したらi+=1する
            count[i] += 1
        i += 1  # アルファベットがa,b,cと続くと同時にcountのiを＋１することでcount内の要素に順番にアクセスする
for i in range(26):  # iが1ずつ増えるを繰り返す
    print(alphabet[i] + " : " + str(count[i]))
