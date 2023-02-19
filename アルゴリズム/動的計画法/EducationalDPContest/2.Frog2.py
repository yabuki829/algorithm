# https://atcoder.jp/contests/dp/tasks/dp_b

# 5 3
# 10 30 40 50 20

# dpの初期値をかなり大きくしておかないと初期値より大きいコストが出た時にエラーになる
# 「10^5」やとエラー出た

n,K = map(int,input().split())
h = list(map(int,input().split()))

dp = [float("inf")] * n
dp[0] = 0
dp[1] = abs(h[0]-h[1])

for i in range(2,n):
  # 1~kまで値を比べたい
  
  for k in range(1,K+1):
    # 移動先が範囲外でないかどうか
    if k < len(h):
      cost = dp[i-k] + abs(h[i-k]-h[i])
      dp[i] = min(dp[i],cost)

print(dp[-1])



