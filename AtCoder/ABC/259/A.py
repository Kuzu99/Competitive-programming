# A - Growth Record

# N歳の誕生日 Tcm
# 0~X 毎年Dcm伸びでた
# X ~ N歳まで変化なし
# M歳の誕生日身長が何cmだったか

# 38 20 17 168 3
# 38歳 168cm
# 17歳まで毎年3cm伸びでた
# 17 ~ 38まで変化なし
# 20歳の時の誕生日？cmだった


# input
from re import T


n, m, x, t, d = list(map(int, input().split()))

# calc
if x <= m:
    ans = t
else:
    ans = t - d*(x-m)

# output
print(ans)
