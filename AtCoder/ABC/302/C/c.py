# ABC 302 C
# https://atcoder.jp/contests/abc302/tasks/abc302_c
from __future__ import annotations
from collections import defaultdict

n, m = map(int, input().split())
s = [input() for _ in range(n)]

graph: dict[int, list[int]] = {}
for i in range(n):
    graph[i] = []

# それぞれの単語通しの差分から、1文字の差異しかないものを結ぶグラフを作る
for i in range(n-1):
    for j in range(i+1, n):
        i_str = s[i]
        j_str = s[j]

        counter = 0
        for k in range(m):
            if i_str[k] != j_str[k]:
                counter += 1
                if counter > 2:
                    counter = 0
                    break
        if counter == 1:
            graph[i].append(j)
            graph[j].append(i)

# [print(node, graph[node]) for node in graph.keys()]
# 一筆書きできたら　ＯＫ
flag = False


def dfs(graph, start, visited):
    global flag
    new_visited = visited.copy()  # ミュータブルオブジェクトは参照渡しされてしまうのでコピーを生成する
    new_visited.add(start)

    if flag == True:
        return

    if len(new_visited) == len(graph):
        # ゴールしたので終わる
        # print('Goal', new_visited)
        flag = True
        return

    for neighbor in graph[start]:
        # print('visit: ', start, new_visited, graph[start], 'neighbor:', neighbor, neighbor not in new_visited)
        if neighbor not in new_visited:
            # print('  path:', start, 'to', neighbor)
            dfs(graph, neighbor, new_visited)


def is_eulerian(graph: dict[int, list[int]]):
    global flag
    # 全ての頂点を始点としてgraphが連結であることを確認する（深さ優先探索を利用）
    for start in graph:
        if flag == True:
            return

        # print("start: " + str(start))
        visited = set()
        dfs(graph, start, visited)


is_eulerian(graph)
if flag:
    print('Yes')
else:
    print('No')
