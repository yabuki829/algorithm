N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


# Aを回転させることでA[i][j] == 1 and B[i][j] == 1であるか判別する


# 90度右回転
# 1. 上下逆転
# 2. 列と行の入れ替え

def rotete(A):
  # print("回転します")
  A = A[::-1]
  routate_A = []
  for x in zip(*A):
    routate_A.append(x)
    
  return  routate_A

for _ in range(4):
  for i in range(N):
    for j in range(N):
      # 判定
      if A[i][j] == 1 and B[i][j] == 0:
        break
    else:
      continue
    break
  else:
    # breakが呼ばれなかった
    print("Yes")
    exit()
  # 90度回転させる
  A = rotete(A)
     
print("No")


# ------------------------------------------
import numpy as np
# 入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
# NumPy配列への変換
A = np.array(A)
B = np.array(B)

for _ in range(4):
  # 90度回転
  A = np.rot90(A)
  flag = True
  for i in range(N):
    for j in range(N):
      if A[i][j] == 1 and B[i][j] == 0:
        flag = False

  if flag:
    print("Yes")
    exit()

print("No")
