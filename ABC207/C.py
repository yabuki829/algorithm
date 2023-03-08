n = int(input())

L = [-1] * n
R = [-1] * n
def convert(t,l,r):
  if t == 1:
    return l , r
  elif t == 2:
    return l, r-0.5
  elif t == 3:
    return l+0.5,r 
  elif t == 4:
    return l+0.5,r-0.5

# 入力
for i in range(n):
  t,l,r = map(int,input().split())
  L[i],R[i] = convert(t,l,r)

ans = 0
for i in range(n):
  a,b = L[i],R[i] 
  for j in range(i+1,n):
    c,d = L[j],R[j]
    if not (R[i] < L[j] or R[j] < L[i]):
      ans +=1

print(ans)

