S = input()

# RNBQKBNR

# K,Qの数が１文字
# R, B, N がちょうど 2 文字ずつ

# 1.Bの位置が偶数と奇数になる
# 2.KはRの間にある

isOK = False
# ぐうきのチェック
for x in range(7):
  for y in range(x + 1, 8):
    if S[x] == 'B' and S[y] == 'B' and (x % 2) != (y % 2):
      isOK = True
      break



# KはRに中にある
isOK2 = False 
for x in range(7):
  for y in range(x + 1, 8):
     if S[x] == 'R' and S[y] == 'R' :
      for z in range(x,y):
        if S[z] == "K":
          isOK2 = True
          break

if isOK and isOK2 :
  print("Yes")
else:
  print("No")