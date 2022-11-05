# https://atcoder.jp/contests/abc276/tasks/abc276_b

m, n = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

# 都市毎に配列を用意する
# cities[index-1] = [道先の都市]
cities = [[] for _ in range(m)]

# d[i] 道先の都市をcitiesに入れる
for path in d:
    cities[path[0]-1].append(path[1])
    cities[path[1]-1].append(path[0])

for city in cities:
    city.sort()
    if (len(city) != 0):
        print(len(city), end=' ')
        print(' '.join(map(str, city)))
    else:
        print(len(city))
