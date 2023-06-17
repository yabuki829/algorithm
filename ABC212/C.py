# https://atcoder.jp/contests/abc212/tasks/abc212_c
n,m = map(int,input().split())
inf = float("inf")
A = list(map(int,input().split())) + [inf,-inf]
B = list(map(int,input().split()))
A.sort()
B.sort()

min_ans = inf
# A,Bから一つずつ要素を選んだ時、2つの値の差が最小である値を求める

# 6 8
# 82 76 82 82 71 70
# 17 39 67 2 45 35 22 24

# 2分探索でいけそう


import bisect 
for x in B: 
  index = bisect.bisect_left(A,x)
  num_1 = abs(A[index] - x)
  num_2 = abs(A[index-1] - x)

  min_ans = min(min_ans,min(num_1,num_2))

print(min_ans)

# 理解度A
# 二分探索