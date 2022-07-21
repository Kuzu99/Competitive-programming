# A - A to Z String 
# https://atcoder.jp/contests/abc257/tasks/abc257_a 

n, x = list(map(int, input().split()))
ans_inedx = (x-1)//n
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = alf[ans_inedx]
print(ans)
