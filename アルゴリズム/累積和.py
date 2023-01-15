# 10 5
# 8 6 9 1 2 1 10 100 1000 10000
# 2 3
# 1 4
# 3 9
# 6 8
# 1 10

# 売上
# 8 6 9 1 2 1 10 100 1000 10000
# 売上の累計
# 1日目は8,2日目は14,3日目は23
# 8 14 23 ..... X

# L日目からR日目までの売上を求めるには 
# * R日目までの売上 - L-1日目までの売上

N,Q = map(int,input().split())
A = list(map(int,input().split()))

L = [ None ] * Q
R = [ None ] * Q

for i in range(Q):
  L[i],R[i] = map(int,input().split())
  
# -- 累積和の計算--
S = [None] * (N+1)
# １日目の売り上げは0円
S[0] = 0

for i in range(N):
  S[i+1] = S[i] + A[i]
# --------------
for i in range(Q):
  r = S[R[i]]
  l = S[L[i] - 1]
  
  print(r-l)


