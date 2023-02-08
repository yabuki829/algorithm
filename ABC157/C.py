# 3 3
# 1 7
# 3 2
# 1 7


n,m = map(int, input().split())
# n =< 3
# s =< 3
sc = [list(map(int, input().split())) for i in range(m)]


for i in range(1000):
  flag = True
  ans = str(i)
  # 桁数が違う時はスキップする
  if len(ans) != n:
    continue

  for j in range(m):
    # 桁,数
    si,ci = sc[j]
    # 条件を満たさなければ flagをFalseに変更する
    if int(ans[si-1]) != ci:
      flag = False
      
  if flag:
    print(ans)
    exit(0)

print(-1)

