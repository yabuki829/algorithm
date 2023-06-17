# https://atcoder.jp/contests/abc211/tasks/abc211_d
# 4 5
# 2 4
# 1 2
# 2 3
# 1 3
# 3 4
import collections
# N が都市の数
# M が道路の数
N,M = map(int,input().split())
MOD = 10 ** 9 + 7

Graph = [list() for i in range(N+1)]

A = [ None ] * M
B = [ None ] * M

for i in range(M):
	A[i], B[i] = map(int, input().split())
# 隣接リストの作成

for i in range(M):
  Graph[A[i]].append(B[i])
  Graph[B[i]].append(A[i])

# 時間を記録しておく
visited = [-1] * (N+1) 
dp = [0] * (N+1)

q = collections.deque()
q.append(1)

visited[1] = 1
dp[1] = 1

while len(q) != 0:
  now = q.popleft()

  for next in Graph[now]:

    if visited[next] == -1:
      visited[next] = visited[now] + 1
      q.append(next)
    if visited[next] == visited[now] + 1:
        dp[next] += dp[now] 
        dp[next] %= MOD

# 最短経路は何通りある？

print(dp[-1])
# 幅優先探索 + DP
# 理解度B


# 0    1    2  
#--------------
#   -> 3 -> 
# 1          4
#   -> 2 -> 