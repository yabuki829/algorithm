# https://atcoder.jp/contests/abc156/tasks/abc156_d

n,a,b = map(int, input().split())

# n種類の花を持っている
# a,b本の花は作れない。
# 作れる花束の数は何種類？
# 
# n ≤ 10^9
# 4 1 3


# 組み合わせは、
# 全部で　2^n - 1通りある。

#そこから nCa通り, nCb通りの組み合わせを除く
# 2^n - 1 - nCa　- nCb

def solve():
  pass
  

solve()


