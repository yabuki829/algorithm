
# https://atcoder.jp/contests/abc203/tasks/abc203_b
# 1 2 -> 

n,k = map(int,input().split())

ans = 0

# 部屋数はn*k個


for i in range(n):
  for j in range(k):
    ans +=  100*(i+1) + (j+1)

print(ans)


