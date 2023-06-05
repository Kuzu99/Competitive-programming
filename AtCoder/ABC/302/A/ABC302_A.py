# ABC302 A 
# https://atcoder.jp/contests/abc302/tasks/abc302_a

a, b = map(int, input().split())

amari = a % b
show = a // b
kasan = 1
if amari == 0:
    kasan = 0

ans = show + kasan

print(ans)