""" Python 競技プログラミング テクニックまとめ """

""" 入力系 """

# A B
m, n = map(int, input().split())

# A_1 B_1
# A_2 B_2
# A_3 B_3
d = [list(map(int, input().split())) for _ in range(n)]

""" 出力系 """

# 数値のリストを文字列として連結する
cities = [[] for _ in range(m)]
print(' '.join(map(str, cities)))

# 改行しないで出力する
print("text", end="")
