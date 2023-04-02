# https://atcoder.jp/contests/abc209/tasks/abc209_b
# 数番目の商品は定価の 1 円引きの値段で買うことができます。奇数番目の商品は定価で売られています。

# 偶数であれば1円引き買う
# 奇数であれば定価で買う
n,x = map(int,input().split())

A = list(map(int,input().split()))
# 1≤N≤100　なので全列挙? 全探索?で行ける

for i in range(1,n+1):
  # 偶数
  if i % 2 == 0:
    x -= A[i-1] - 1
  else:
    x -= A[i-1]


if x >= 0:
  print("Yes")
else:
  print("No")