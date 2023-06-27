# https://atcoder.jp/contests/abc306/tasks/abc306_b
A = list(map(int,input().split()))

ans = 0
for i in range(64):
  if A[i] == 1: 
     ans += 2**i
  

print(ans)
  