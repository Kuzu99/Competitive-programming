# ABC 303 B 
# https://atcoder.jp/contests/abc302/tasks/abc302_b
from __future__ import annotations

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

class Point_S:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

def isOK(points: list[Point_S]):
    [print(point.i+1, point.j+1) for point in points]
    exit()

def check_up(i:int, j:int):
    if i-4 < 0 or i-4 >= h:
        return

    if s[i-1][j] == 'n' and s[i-2][j] == 'u' and s[i-3][j] == 'k' and s[i-4][j] == 'e':
        s_list = [Point_S(i-n, j) for n in range(5)]
        isOK(s_list)
    
    
def check_up_right(i:int, j:int):
    if i-4 < 0 or i-4 >= h or j+4 < 0 or j+4 >= w:
        return
    
    if s[i-1][j+1] == 'n' and s[i-2][j+2] == 'u' and s[i-3][j+3] == 'k' and s[i-4][j+4] == 'e':
        s_list = [Point_S(i-n, j+n) for n in range(5)]
        isOK(s_list)
    
def check_right(i:int, j:int):
    if i < 0 or i >= h or j+4 < 0 or j+4 >= w:
        return
    if s[i][j+1] == 'n' and s[i][j+2] == 'u' and s[i][j+3] == 'k' and s[i][j+4] == 'e':
        s_list = [Point_S(i, j+n) for n in range(5)]
        isOK(s_list)
    
def check_down_right(i:int, j:int):
    if i+4 < 0 or i+4 >= h or j+4 < 0 or j+4 >= w:
        return
    
    if s[i+1][j+1] == 'n' and s[i+2][j+2] == 'u' and s[i+3][j+3] == 'k' and s[i+4][j+4] == 'e':
        s_list = [Point_S(i+n, j+n) for n in range(5)]
        isOK(s_list)
    
def check_down(i:int, j:int):
    if i+4 < 0 or i+4 >= h or j < 0 or j >= w:
        return

    if s[i+1][j] == 'n' and s[i+2][j] == 'u' and s[i+3][j] == 'k' and s[i+4][j] == 'e':
        s_list = [Point_S(i+n, j) for n in range(5)]
        isOK(s_list)

def check_down_left(i:int, j:int):
    if i+4 < 0 or i+4 >= h or j-4 < 0 or j-4 >= w:
        return
    
    if s[i+1][j-1] == 'n' and s[i+2][j-2] == 'u' and s[i+3][j-3] == 'k' and s[i+4][j-4] == 'e':
        s_list = [Point_S(i+n, j-n) for n in range(5)]
        isOK(s_list)
    
def check_left(i:int, j:int):
    if i < 0 or i >= h or j-4 < 0 or j-4 >= w:
        return
    
    if s[i][j-1] == 'n' and s[i][j-2] == 'u' and s[i][j-3] == 'k' and s[i][j-4] == 'e':
        s_list = [Point_S(i, j-n) for n in range(5)]
        isOK(s_list)
    
def check_up_left(i:int, j:int):
    if i-4 < 0 or i-4 >= h or j-4 < 0 or j-4 >= w:
        return
    
    if s[i-1][j-1] == 'n' and s[i-2][j-2] == 'u' and s[i-3][j-3] == 'k' and s[i-4][j-4] == 'e':
        s_list = [Point_S(i-n, j-n) for n in range(5)]
        isOK(s_list)
    
s_points: list[Point_S] = []

# 横
for i in range(h):
    for j in range(w):
        if s[i][j] == 's':
            s_points.append(Point_S(i, j))
 
for s_point in s_points:
    check_up(s_point.i, s_point.j) # 上
    check_up_right(s_point.i, s_point.j)# 右上
    check_right(s_point.i, s_point.j) # 右
    check_down_right(s_point.i, s_point.j) # 右下
    check_down(s_point.i, s_point.j) # 下
    check_down_left(s_point.i, s_point.j) # 左下
    check_left(s_point.i, s_point.j) # 左
    check_up_left(s_point.i, s_point.j) # 左上
