# 連列グラフかどうかを判別

# n,m = 4 3
# 1 3
# 4 2
# 3 2

# 1. グラフ探索
n,m = map(int,input().split())
node = [[] for _ in range(n)]


for i in range(m):
  u, v = map(int, input().split())
  # スタートを0にしたいので -1してる
  u -= 1
  v -= 1 
  node[v].append(u)
  node[u].append(v)

visited = [False for _ in range(n)]

def dfs(now):
    visited[now] = True
    for i in node[now]:
        if not visited[i]:
            dfs(i)

dfs(0)
  
if all(visited):
  print("連結グラフです")


