# 回文問題

n = int(input())
A = list(map(int,input().split()))

chars = set(A)

parent = [-1] * 220000

# xの親を返す
def find(x):
  if parent[x] < 0:
    return x
  else:
    parent[x] = find(parent[x])
    return parent[x]

answer = 0
def unite(x,y):
  x = find(x)
  y = find(y)

  # 同じ親を持つ場合は統合しない
  if x == y:
    return 
  parent[x] += parent[y]
  parent[y] = x

for i in range(n):
  l = i
  r = n-i-1
  if l < r:
    # 親が同じでない場合unite
    # print("-------",A[l],A[r],"です","-------")
    # print("A[l]の親は",find(A[l]),"A[r]の親は",find(A[r]))
    if find(A[l]) != find(A[r]):
      # print("親が同じでないのでuniteします")
      answer+=1
      unite(A[l],A[r])
    # print("-----------------------")

print(answer)

# グラフ unionfind


