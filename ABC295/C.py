n = input()

A = list(map(int,input().split()))

#  出現頻度を調べる
import collections


A_set = list(set(A))
A_counter = collections.Counter(A)
ans = 0
for a in A_set:
  ans += A_counter[a] // 2 
print(ans)

# 解けた