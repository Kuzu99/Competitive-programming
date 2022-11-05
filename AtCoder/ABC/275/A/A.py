# https://atcoder.jp/contests/abc275/tasks/abc275_a

s = int(input())
h = list(map(int, input().split()))

max_value = -1
max_index = -1

for index in range(len(h)):
    if(max_value < h[index]):
        max_index = index
        max_value = h[index]

print(max_index + 1)