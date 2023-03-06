# 7 3
# 2 0 2 3 2 1 9


N,K = map(int,input().split())
A = list(map(int,input().split()))

max = 0
A = list(set(A))
print(A[0])