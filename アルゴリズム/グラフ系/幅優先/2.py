# 幅優先はQueを使う
# 頂点1からの最短距離


# 5 5
# 1 2
# 1 3
# 3 2
# 5 2
# 4 2

import queue
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for i in range(M):
	G[A[i]].append(B[i])
	G[B[i]].append(A[i])

dict = [ -1 ] * (N + 1)
# queueを宣言
Q = queue.Queue()
dict[1] = 0
# 最初1を追加する
Q.put(1)

# Qが空になるまで続ける
while not Q.empty():
  # 先頭の要素を取り出す
  now = Q.get()
  print("------------------")
  print("現在は",now,"にいます")
  flag = False
  for next in G[now]:
    # 訪れていなければ
    if dict[next] == -1:
      print(next,"に行くことができます")
      # dict[now] は　nowに行くのにかかった距離
      dict[next] = dict[now] + 1
      Q.put(next)
      flag = True

  if flag == False:
      print(now,"から行ける場所がありませんでした。")

print(dict)


for i in range(1,N+1):
  print(dict[i])

#     1
#    /  \
#   2 -- 3
#  / \
# 4   5  