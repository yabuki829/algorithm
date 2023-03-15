# https://atcoder.jp/contests/abc208/tasks/abc208_d
# このコードではTLEする 3/15
N,M = map(int,input().split())

inf= float("inf")

list = [[inf]*N for _ in range(N)]

# 出発地点と目的地が同じであれば0を入れる
for i in range(N):
  list[i][i] = 0


for i in range(M):
  # 出発地点 -> 目的地  所要時間
  a,b,c = map(int,input().split())
  list[a-1][b-1] = c



# for line in list: 
#   print(line)

#    1  2    3
# 1 [0, 3, inf]
# --------------
# 2 [inf, 0, 2]
# --------------
# 3 [inf, inf, 0]


ans = 0

for k in range(N):
  for s in range(N):
    for t in range(N):
      a = list[s][t]
      b = list[s][k] + list[k][t]
      list[s][t] = min(a,b)

      if list[s][t] < float("inf"):
        ans += list[s][t]


print(ans)


# ワーシャルフロイド法 O(N^3)