# 完全グラフかどうかの判別 # 172 452

# 5 5
# 1 2
# 1 3
# 3 2
# 5 2
# 4 2

# 頂点と辺
N,M = map(int,input().split())

# a と b を双方向に結んでいる。
A = [None] * M
B = [None] * M

# N−1 ≤ M
for i in range(M):
  A[i], B[i] = map(int,input().split())

# グラフの頂点の関係をリストで表現する。
Graph = [list() for i in range(N+1)]


for i in range(M):
  print(i,"回目",A[i],B[i])
  Graph[A[i]].append(B[i]) 
  Graph[B[i]].append(A[i]) 


print(Graph)

# 頂点に訪れたかどうか
visited = [False] * (N+1)
# スタック
S = list()
# スタート地点なのでTrueにする
visited[1] = True
# スタート地点に1を入れる
S.append(1) 

# 深さ優先探索

def dfs():
  while len(S) >= 1:
    # 調べる対象を取り出す
    # スタックなので一番最後に追加したやつから調べる
    now = S.pop()
    print("---------------------------------")
    print("現在",now,"にいます")
    # 行ける場所があるかどうかのFlag Trueなら行ける場所がある
    flag = False
    for next in Graph[now]:
      # まだ訪れてなければ
      if visited[next] == False:
        visited[next] = True
        print(next,"に行くことができます。")
        S.append(next) 
        flag = True

    if flag == False:
      print(now,"から行ける場所がありませんでした。")
  answer = True

  # 0番目はスタート地点なので範囲は1,N+1 にする
  print("訪れた場所",visited)
  for i in range(1,N+1):
    if visited[i] == False:
      answer = False

  if answer:
    print("すべてに訪れました。")
  else:
    print("訪れてないところがあります。")
    

dfs()



