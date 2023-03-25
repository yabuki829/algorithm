# https://atcoder.jp/contests/typical90/tasks/typical90_d


H,W = map(int,input().split())

A = []
# 4000000 = 4*10^6

# [0][i] i行目の合計が入ってる 　
# [1][j] j列目の合計が入ってる 
A_result = [[0]*H ,[0]*W]

# h行の合計をする
for i in range(H):
  a = list(map(int,input().split()))
  A.append(a)
  A_result[0][i] = sum(a)



# 列の合計をする
for i in range(W):
  sum_h = 0
  for j in range(H):
    sum_h+=A[j][i]

  A_result[1][i] = sum_h

# print(A_result)

for i in range(H):
  for j in range(W):
    print(A_result[0][i] + A_result[1][j] - A[i][j],end=" ")
  print()

# 計算結果　前処理
# 星2 199~399  