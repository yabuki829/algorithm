# 部分和問題
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
# 3 7
# 2 2 3


N,S = map(int,input().split())
A = list(map(int,input().split()))

dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True
for i in range(1, S+1):
	dp[0][i] = False

# 動的計画法
# iは選ぶカードの枚数 
# jは合計のこと
# dp[i][j] は i枚選んだ時に合計jになるか

for i in range(1,N+1):
  for j in range(0,S+1):

    # A[i-1]枚目のカードが合計jより大きい場合
    if j < A[i-1]:
      # 一行前がTrueであればdp[i][j]はTrue
      
      if dp[i-1][j] == True:
        # i枚選んだ時に合計jになるか
        dp[i][j] = True
      else:
        dp[i][j] = False

    # A[i-1]枚目のカードが合計j未満
    if j >= A[i-1]:

      if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
        dp[i][j] = True
      else:
        dp[i][j] = False

# for i in range(N+1):
#   print(dp[i])

if dp[N][S]:
  print("Yes")
else:
  print("No")