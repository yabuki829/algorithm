# https://atcoder.jp/contests/typical90/tasks/typical90_c
# https://twitter.com/e869120/status/1377752658149175299/photo/1
# グラフの直径を求める　 直径とは「最も遠い頂点間の距離」
n = int(input())

# スタート地点から一番離れたところから　スタート地点に道を作るれば通る道の数が最大になる

graph = [[] for i in range(n)]

for _ in range(n-1):
  a,b = map(int,input().split())
  a -= 1 
  b -= 1
  graph[a].append(b)
  graph[b].append(a)

import sys
sys.setrecursionlimit(10**7)



#距離を記録しておく
distance = [0] * n

def dfs(x,last=-1):
  for to in graph[x]:
    if to == last:
      continue

    distance[to] = distance[x] + 1
    dfs(to,x)


dfs(0)

# 一番遠いところまでの距離
max_dist = max(distance)

farest_index = distance.index(max_dist)
distance[farest_index] = 0
dfs(farest_index)


print(max(distance) + 1)

# 木　深さ優先 dfs グラフ