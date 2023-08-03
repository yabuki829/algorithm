n,p,q  = map(int,input().split())

D = list(map(int,input().split()))


min_cost = p
for i in range(n):
  if p > D[i] + q:
    min_cost = min(min_cost,D[i]+q)


print(min_cost)

