A = [list(map(int, input().split())) for i in range(3)]

n = int(input())
B = [int(input()) for i in range(n)]

# 1 <= b <= 100

# 84 97 66
# 79 89 11
# 61 59 7

# 7

# 89
# 7
# 87
# 79
# 24
# 84
# 30

# -1 97 66
# 79 89 11
# 61 59 7

def checkBingo(A):
  # 8パターン確認する
  # 行を確認
  if A[0][0] == -1 and A[0][1] == -1 and A[0][2] == -1 :
    return "Yes"  
  if A[1][0] == -1 and A[1][1] == -1 and A[1][2] == -1:
    return "Yes"
  if A[2][0] == -1 and A[2][1] == -1 and A[2][2] == -1:
    return "Yes"

  # 列を確認する　
  if A[0][0] == -1 and A[1][0] == -1 and A[2][0] == -1 :
    return "Yes"
  if A[0][1] == -1 and A[1][1] == -1 and A[2][1] == -1 :
    return "Yes"
  if A[0][2] == -1 and A[1][2] == -1 and A[2][2] == -1 :
    return "Yes"
  # 斜めを確認する

  if A[0][0] == -1 and A[1][1] == -1 and A[2][2]:
    return "Yes"
  if A[0][2] == -1 and A[1][1] == -1 and A[2][0]:
    return "Yes" 

  return "No"

for b in B:
  for i in range(3):
    for j in range(3):
      if b == A[i][j]:
        # 数字を消す
        A[i][j] = -1
        break

print(checkBingo(A))


