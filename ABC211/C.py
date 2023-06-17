# https://atcoder.jp/contests/abc211/tasks/abc211_c
S = input()
chokudai = "chokudai"
dp = [0 for _ in range(9) ]  
dp[0] = 1
mod = 10**9+7

for i in range(len(S)):
  for j in range(8):
    if S[i] == chokudai[j]:
      dp[j+1] += dp[j] 
      # dp[j+1] %= mod

print(dp[8])
# 理解度B
# DP問題　動的計画法

"""
    a b c a b a b c
a   1 1 1 2 2 3 3 3
ab  0 1 1 1 3 3 6 6
abc 0 0 1 1 1 1 1 2

"""