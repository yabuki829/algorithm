# 3
# 1 2 2
# 3 1 2
# 2 3 2
from collections import Counter

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))


count_A = Counter(A)

ans = 0

for c in C:
  # スタートと0からにするために,-1にしている
  #B_C_j は B[C[j]]のこと
  B_C_j = B[c-1]

  # A に B[C[j]]の出現回数を足す
  ans += count_A[B_C_j]

print(ans)


