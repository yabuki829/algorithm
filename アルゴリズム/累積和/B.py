# 二次元の累積和問題
# 横方向に累積和をとり縦方向の累積和をとる
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h

# 2 0 0 5 1
# 1 0 3 0 0
# 0 8 5 0 2
# 4 1 0 0 6
# 0 9 2 7 0

def solve4():
  H,W = map(int,input().split())
  x = [None] * H

  for i in range(H):
    x[i] = list(map(int,input().split()))
    
  q = int(input())
  
  A = [0] * q
  B = [0] * q
  C = [0] * q
  D = [0] * q
  
  for i in range(q):
    A[i],B[i],C[i],D[i] = map(int,input().split())
  
  # 0,0 ~ H,Wの総和のデータを作成
  # [ ポイント ]i-1,j-1しても範囲外にならないように+1してる
  data = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
  # 縦方向
  for i in range(1,H+1):
    for j in range(1,W+1):
      # xの配列のスタートは1ではなく、0なのでx[i-1][j-1]
      data[i][j] = data[i][j-1] + x[i-1][j-1]
  

  # 縦方向
  for i in range(1,W+1):
    for j in range(1,H+1):
      data[i][j] = data[i-1][j] + data[i][j]
  
  # 答えを出す
  for i in range(q):
    print(data[C[i]][D[i]] + data[A[i]-1][B[i]-1] - data[A[i]-1][D[i]] - data[C[i]][B[i]-1])
solve4()
