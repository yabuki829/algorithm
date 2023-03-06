# 3 2
# 10 20 30
# 1 3

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for b in B:
  ans += A[b-1]
print(ans)