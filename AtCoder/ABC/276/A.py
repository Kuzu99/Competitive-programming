# Atcoder Beginner Contest 276 A
# https://atcoder.jp/contests/abc276/tasks/abc276_a

s = input()

# 文字列を後ろから検索していき最初にaを見つけたらそれを出力する

s_len = len(s)

for index in range(s_len):
    if s[s_len - 1 - index] == 'a':
        print(s_len - index)
        break
else:
    print(-1)