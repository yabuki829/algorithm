# https://atcoder.jp/contests/abc296/tasks/abc296_d

n,m = map(int,input().split())

# XはM以上で ともにN以下のa*bで表すことができる

# N,M <= 10^12
# 5,7
# M以上のXをともにN以下のa*bで表すことができる?


# 1 <= a,b <= N

import math
# 最大値が間違ってた
ans = 10**24
# ans = 10**12
# a は　1 ~ √m 　までやる
for a in range(1,math.ceil(m**0.5)+1):
  # 切り上げ m /a の切り上げ
  b = -(-m//a)

  if 1 <= a <= n  and 1 <= b <= n:
    ans = min(ans,a*b)
  
if ans == 10**24:
  print(-1)
else:
  print(ans)