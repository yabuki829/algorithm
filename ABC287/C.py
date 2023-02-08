# グラフ問題
# https://atcoder.jp/contests/abc287/tasks/abc287_c

# パスグラフの条件は

# 1. すべての辺が連結している。　
# 2. すべての頂点に対して辺が1本または、2本である。
# 3. 辺の数が1本の頂点が2点ある。

# 1が満たしているかどうかの判定は,dfs ,bfs unionfindがある。

# 4 3
# 1 3
# 4 2
# 3 2

n,m = map(int,input().split())
node = [[] for _ in range(n)]

for i in range(m):
  u, v = map(int, input().split())
  # スタートを0にしたいので -1してる
  u -= 1
  v -= 1 
  node[v].append(u)
  node[u].append(v)

# グラフが連結かどうか調べる
visited = [False for _ in range(n)]
# print(node)

def dfs(now):
    visited[now] = True
    for i in node[now]:
        if not visited[i]:
            dfs(i)

dfs(0)

# 1. すべての辺が連結している
if not all(visited):
  print("No")
  exit()

# 2. すべての頂点に対して辺が1本または、2本である。
# 辺の数が1本の頂点の数
c = 0 
# print(node)
for x in node:
  if len(x) == 1:
    c += 1 
  # 2以外であれば終了
  elif len(x) != 2 :
    print("No")
    exit()

# 3. 辺の数が1本の頂点が2点ある。
if c == 2:
    print("Yes")
else:
    print("No")
