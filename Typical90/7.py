# https://atcoder.jp/contests/typical90/tasks/typical90_g


from bisect import bisect_left
N = int(input())
A = [- 10**18 ] + list(map(int,input().split())) + [ 10**18 ]
q = int(input())
A.sort()

for _ in range(q):
  b = int(input())
  index = bisect_left(A,b)
  # 一個次
  nxt = A[index]
  # 一個前
  prev = A[index-1]

  print(min(nxt - b, b - prev))


# 二分探索 