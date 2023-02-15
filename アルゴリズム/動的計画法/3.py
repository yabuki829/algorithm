# ------------------------------------------------
# 動的計画法
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

# N = 5 
# a = 2 4 1 3
# b = 5 3 7  
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [None] * (N + 1) 
print(dp)
dp[1] = 0
dp[2] = a[0]

# 2までdpに入力しているので3スタート
for i in range(3,N+1):
  # 一個前か
  # 2個前からの移動
  one = dp[i-1] + a[i-2]
  two = dp[i-2] + b[i-3]
  dp[i] = min(one,two)

print(dp) # [None,0, 2, 5, 5, 8]

