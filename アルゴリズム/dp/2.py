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




# ------------------------------------------------
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