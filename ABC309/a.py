A, B = map(int,input().split())

# 左右に隣接
# 真ん中の場合


if B == 2 or B == 5 or B == 8:
  A,B = B,A
 
if A == 2:
  if B == 1 or B == 3:
    print("Yes")
    exit()

if A == 5:
  if B == 4 or B == 6:
    print("Yes")
    exit()

if A == 8:
  if B == 7 or B == 9:
    print("Yes")
    exit()

print("No")