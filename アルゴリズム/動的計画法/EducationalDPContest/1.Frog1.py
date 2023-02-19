# https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = list(map(int,input().split()))

dp = [None] * N
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2,N):
  one = dp[i-1] + abs(h[i-1]-h[i])
  two = dp[i-2] + abs(h[i-2]-h[i])
  dp[i] = min(one,two)

print(dp[-1])