# https://atcoder.jp/contests/abc309/tasks/abc309_b
n = int(input())

A = []
for _ in range(n):
    row = input()
    A.append(list(row))


num = A[0][n-1]



# 上
for j in range(n-1,0,-1):
    if j == 0:
        continue
    A[0][j] = A[0][j-1]



# 左
for i in range(n-1):
    if i == n-1:
        continue
    A[i][0] = A[i+1][0]


# 下
for j in range(n-1):
    if j == n-1:
        continue
    A[n-1][j] = A[n-1][j+1]


    
# 右
for i in range(n-1,0,-1):
    if i == 0:
        continue 
    A[i][n-1] = A[i-1][n-1]


A[1][n-1] = num

for i in range(n):
    print("".join(A[i]))


# 紙にかけば簡単
# 理解度A
