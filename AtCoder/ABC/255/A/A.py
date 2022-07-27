r, c = list(map(int, input().split()))
a11, a12 = list(map(int, input().split()))
a21, a22 = list(map(int, input().split()))

b = [[a11, a12], [a21, a22]]

print(b[r-1][c-1])