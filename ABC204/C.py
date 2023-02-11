# https://atcoder.jp/contests/abc204/tasks/abc204_c
# 一問だけtelだったのでちゃんと通ったコードではない。

# 3 3
# 1 2
# 2 3
# 3 2

# O(n*(n+m)) 2000* (2000+2000) = 80000000 = 8*10^6
# N個の頂点のNiの頂点から行ける頂点の数を数えればok

# グラフを作成する
import queue
n,m = map(int,input().split())


G = [ list() for i in range(n+1) ]
for i in range(m):
  a,b = map(int,input().split())
  G[a].append(b)

def bfs(i):
  visited = [0] * (n+1)
  Q = queue.Queue()
  Q.put(i)
  count = 0
  while not Q.empty():
    now =  Q.get()
    visited[now] = 1
    count += 1

    for next in G[now]:
      if visited[next] == 0: 
        # print(next,"に移動可能です。")
        visited[next] += 1
        Q.put(next)

  return count

ans = 0
for i in range(1,n+1):
  ans += bfs(i)
print(ans)