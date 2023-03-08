N,Q = map(int,(input().split()))
A = list(map(int,input().split()))


def cnt(m):
  left = 0
  right = N

  while  right - left > 1:
    mid = (left + right) // 2
    if A[mid]<=m:
      left = mid
    else :
      right = mid
  if m < A[0]:
    right = 0
  return m - right


def binary_search(k):
  left = 0
  right = 10**19

  while right - left > 1:
    mid = (left + right) // 2
    if cnt(mid)<k:
      left = mid
    else :
      right = mid

  return right
      


for _ in range(Q):
  k = int(input())
  print(binary_search(k))



# 二分探索