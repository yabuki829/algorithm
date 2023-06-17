# https://atcoder.jp/contests/typical90/tasks/typical90_h


# 順番を変えずにS[i]を取り出してatcoderになるのが何パターンあるか
# N < 100000
N = int(input())
S = input()

# 全探索はNが大きいので明らかにtelする



# 正解はDP


atcoder = "atcoder"
dp = [0 for _ in range(8) ]  
dp[0] = 1
mod = 10**9+7
for i in range(N):
  for j in range(7):
    if S[i] == atcoder[j] :
      dp[j+1] += dp[j] 
      dp[j+1] %= mod

print(dp[7])
# 状態DP

# 類題　https://atcoder.jp/contests/abc211/tasks/abc211_c
