# https://atcoder.jp/contests/abc202/tasks/abc202_d
#  A個の a と B 個の b からなる長さ A+B の文字列のうち、
#  辞書順で K 番目のものを求めてください。

# 入力 
# A B K 
# 2 2 4  -> baab

import math
def comb(n,r):
  return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

a,b,k = map(int,input().split())

# 1.1文字目がaの個数は -> ( (a-1)+b) C(a-1)
# 2.K <=  (a-1)+b) C(a-1) であれば 先頭の文字は "a" になる

ans = ""

# aの個数とbの個数がどちらかが0になれば終了する
while a > 0 and b > 0:
  # aの個数を調べる
  a_comb = comb(a-1+b,a-1)

  # K が aの個数より小さければ,先頭はaである
  if a_comb >= k:
    ans += "a"
    a -= 1
  else:
    ans += "b"
    b -= 1  
    k -= a_comb

# 残りの文字を辞書順で足す
ans += "a" * a
ans += "b" * b 

print(ans)




