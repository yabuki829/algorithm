# 動的計画技法
# 問題を部分問題に分割して、小さい部分問題から大きい部分問題を解いていく手法

# ナップサック問題
# スケジューリング問題

# 問題　https://atcoder.jp/contests/dp/tasks/dp_a
N = 7
h = [2,9,4,5,1,6,10]
# dp[i] は　iに行く最小コスト
# h0番目に行く最小コストはスタート地点なので０
dp = [0]

for i in range(1,N):
  if i == 1:
    dp.append(abs(h[i] - h[0]))
  else:
    # 一個前までのコスト　+　 一個前から現在の場所までのコスト
    hi_1 = dp[i-1] + abs(h[i] - h[i-1])
    hi_2 = dp[i-2] + abs(h[i] - h[i-2])
    minValue = min(hi_1,hi_2)
    
    dp.append(minValue)
    
print(dp) # -> [0, 7, 2, 3, 5, 4, 8] 
print(dp[N-1]) # -> 8

# ナップサック問題
#　問題 https://atcoder.jp/contests/dp/tasks/dp_d