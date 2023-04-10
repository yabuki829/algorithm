# ダイクストラ法
# 参考　
# [ヨビノリさん]https://www.youtube.com/watch?v=X1AsMlJdiok

# 最短経路を導き出せる
# [東大資料] http://bin.t.u-tokyo.ac.jp/szemi21/file/02_suzuki.pdf

# 入力 無効グラフ
# 9 12
# 0 1 4
# 0 2 1
# 0 4 7
# 1 3 2
# 2 5 3
# 3 4 2
# 5 4 2
# 4 7 1
# 3 6 3
# 5 8 7 
# 6 7 2
# 7 8 3

# --------自分で作成したコード------
import heapq
N,M = map(int,input().split())
graph = [ list() for i in range(N) ]


for i in range(M):
  u,v,c = map(int,input().split())
  graph[u].append([v,c])
  # graph[v].append([u,c])

# 確定したところ
kakutei = [False for _ in range(N)]

# 現在の最短距離
shortest_dist = [float("inf")] * N
# スタート地点
start = 0
# スタート地点までの最短距離
shortest_dist[start] = 0

# 1番目が 0番目の最短距離 2番目が頂点の番号
q = [[shortest_dist[start],start]]

while len(q)>0:
  # 距離が小さいものを取得する
  dist ,now_pos = heapq.heappop(q)
  kakutei[now_pos] = True
  for next,cost_dist in graph[now_pos]:
    # 確定の場所で or
    # 現在の場所からnextに行くより,別の場所からnext行く方がコストが少ない場合
    if kakutei[next] or shortest_dist[now_pos]+cost_dist > shortest_dist[next]:
      continue
    # nextの最短距離を更新する
    shortest_dist[next] = shortest_dist[now_pos] + cost_dist
    heapq.heappush(q,[shortest_dist[next],next])

print(shortest_dist[-1])



# 入力　有効グラフ
# 6 7
# 1 2 15
# 1 4 20
# 2 3 65
# 2 5 4
# 3 6 50
# 4 5 30
# 5 6 8

# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bl
# このコードだと1問Telする
import heapq
N,M = map(int,input().split())
graph = [ list() for i in range(N) ]

for i in range(M):
  u,v,c = map(int,input().split())
  u-=1
  v-=1
  graph[u].append([v,c])
  graph[v].append([u,c])

kakutei = [False for _ in range(N)]
  # 現在の最短距離
shortest_dist = [float("inf")] * N
start = 0
shortest_dist[start] = 0

  # 1番目が 0番目の最短距離 2番目が頂点の番号
q = [[shortest_dist[start],start]]

while len(q)>0:
    # 距離が小さいものを取得する
    dist ,now_pos = heapq.heappop(q)
    kakutei[now_pos] = True

    for next,cost_dist in graph[now_pos]:
      # 確定の場所で or
      # 現在の場所からnextに行くより,別の場所からnext行く方がコストが少ない場合
      if kakutei[next] or shortest_dist[now_pos]+cost_dist > shortest_dist[next]:
        continue
      # nextの最短距離を更新する
      shortest_dist[next] = shortest_dist[now_pos] + cost_dist
      heapq.heappush(q,[shortest_dist[next],next])

for i in range(N):
  if shortest_dist[i] != float("inf"):
    print(shortest_dist[i])
  else:
    print(-1)


# 先に別の場所からnext行く方がコストが少ないかを確認する
# 少し最適化 ------------------------------------------
import heapq

N, M = map(int, input().split())
graph = [list() for _ in range(N)]
# スタート地点
start = 0
for i in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, c])
    graph[v].append([u, c])

# 現在の最短距離
shortest_dist = [float("inf")] * N
shortest_dist[start] = 0

# 1番目が スタート地点の最短距離 2番目が頂点の番号
q = [(0, start)]

while q:
    # 距離が小さいものを取得する
    dist, now_pos = heapq.heappop(q)
    # 現在保持しているnow_posへの最短距離(shortes_dist[now_post])が最短距離(dist)より短い
    if shortest_dist[now_pos] < dist:
        continue

    for next, cost_dist in graph[now_pos]:
        # 現在の場所からnextに行くより,別の場所からnext行く方がコストが少ない場合
        if shortest_dist[now_pos] + cost_dist < shortest_dist[next]:
            shortest_dist[next] = shortest_dist[now_pos] + cost_dist
            heapq.heappush(q, (shortest_dist[next], next))

for i in range(N):
    if shortest_dist[i] != float("inf"):
        print(shortest_dist[i])
    else:
        print(-1)