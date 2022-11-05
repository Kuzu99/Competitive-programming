# A - When?
# https://atcoder.jp/contests/abc258/tasks/abc258_a

k = int(input())

if k < 60:
    ans = "21:{:0>2}".format(k)
else:
    ans = "22:{:0>2}".format(k-60)

print(ans)