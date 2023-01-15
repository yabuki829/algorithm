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




# 一番簡単な例題
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
# 問題　コイン
#　額面がC1,C2,..., Cm　円の M種類のコインを使って、 N 円を支払うときの、コインの最小の枚数を求めて下さい。
# 各額面のコインは何度でも使用することができます。

# 6 15
# 1 2 7 8 12 50


# 今回の問題は,1,2,7,8,12,50を使って「15」を作る。
M=6
N=15
conins = [1,2,7,8,12,50]

opt = [float("inf")]*(N+1)
# opt[0] = 0
# opt[1] = 1
# opt[2] = 1
# opt[3] = 2 [1,2]
# opt[4] = 2 [2,2]
# opt[5] = 3 [1,2,2]

opt[0] = 0
# aは1~Nまで

for a in range(1,N+1):
  for c in conins:
    if a >= c:
      opt[a] = min(opt[a-c]+1,opt[a]) 

if opt[N] == float("inf"):
  print("作成できませんでした")
else:
  print(opt[N])



# 足場の問題
# https://atcoder.jp/contests/dp/tasks/dp_a

# 4
# 10 30 40 20
# 足場 i にいるとき、足場 i+1 または i+2 へジャンプする。 このとき、ジャンプ先の足場を j とすると、コスト | hi - hj | を支払う


# 今回の問題は,i番目の足場に行く最小コストを求める

# 足場i+1に移動する
# 足場i+2に移動する
N = int(input())
cost = [float("inf")]*(N)

h = list(map(int,input().split()))
cost[0] = 0

for i in range(1,N):
  # 現在の足場がiだとすると
  # (1) 足場i-1までのコスト + 足場i-1から現在の足場iに移動するコスト
  # (2) 足場i-2までのコスト + 足場i-2から現在の足場iに移動するコスト
  # print("現在の足場",i)
  a = cost[i-1]+abs(h[i]-h[i-1])
  b = cost[i-2]+abs(h[i]-h[i-2])

  cost[i] =  min(a,b)

print(cost[-1])


# 類問題
# https://atcoder.jp/contests/dp/tasks/dp_b
N,K = map(int,input().split())
cost = [float("inf")]*(N)

h = list(map(int,input().split()))
cost[0] = 0

for i in range(1,N):
  # 1~Kまでの足場の移動について考える
  for k in range(1,K+1):
    # kが足場を超えないようにする
    if k < len(h):
    # k個前までの足場のコスト+k個前から現在の足場に移動するコスト
      cost[i] = min(cost[i],cost[i-k]+abs(h[i]-h[i-k]))
    
    
print(cost[-1])

print(max(1,2))