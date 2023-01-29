# 動的計画技法
# 問題を部分問題に分割して、小さい部分問題から大きい部分問題を解いていく手法

# 各段階でいくつかの選択肢がある場合動的計画法を疑う
# ナップサック問題
# 編集距離
# スケジューリング問題　など

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

# ------------------------------------------------
# ナップサック問題
#　問題 https://atcoder.jp/contests/dp/tasks/dp_d
#  参考 https://www.youtube.com/watch?v=gVJ16ThsJYs

N,W=map(int, input().split())
dp=[[0]*(W+1) for i in range(N+1)]

for i in range(1,N+1):
  wi,vi = map(int, input().split())
  
  for w in range(W+1):
    #マイナスであれば選択肢ない
    if w-wi < 0 :
      # 品物を入れない
      dp[i][w] = dp[i-1][w]
    else:
      # (a)i番目の品物を入れない　
      # (b)i番目の品物を入れる
      # a,bのどちらか大きい方
      a = dp[i-1][w]
      b = dp[i-1][w-wi]+vi
      dp[i][w] = max(a,b)
      
  
print(dp[N][W])






