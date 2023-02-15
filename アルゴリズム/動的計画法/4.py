# 動的計画法の復元問題
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q

# 地図の最短経路とかで使ったりする
# 最小のコスト解った後、どの経路が最短なのかを復元する



N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [0] * (N+1)
# スタート位置は今回はdp[1]にしてる
dp[1] = 0
dp[2] = a[0]

for i in range(3,N+1):
  one = dp[i-1] + a[i-2]
  two = dp[i-2] + b[i-3]
  dp[i] = min(one,two)
  
print(dp)


answer = []
# 現在地
now_place = N

while True:
  # 答えに現在地を追加する
  answer.append(now_place)

  # スタート地点に到着したら終了
  if now_place == 1:
    break

  # 1. now_place-1からnow_placeに向かう
  # 2. now_place-2からnow_placeに向かう
  # dp[now_place] と同じ値であれば最適経路

  if dp[now_place-1] + a[now_place-2]== dp[now_place]:
    now_place -= 1
  else:
    now_place -= 2
answer = answer.reverse()
print(answer)