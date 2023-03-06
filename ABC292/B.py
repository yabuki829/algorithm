# 3 9
# 3 1
# 3 2
# 1 2
# 2 1
# 3 1
# 3 2
# 1 2
# 3 2
# 3 3


n,q = map(int,input().split())

isTaijo = [False] * (n+1)
yellowCard = [0] * (n+1)


for _ in range(q):
  i,x = map(int,input().split())
  if i == 1: 
    # xにイエローカードを提示する
    yellowCard[x] += 1
    if yellowCard[x] == 2:
      isTaijo[x] = True
  elif i == 2:
    # xにレッドカードを提示する 
    isTaijo[x] = True
    pass
  else:
    # xが退場しているかどうかを判別する
    if isTaijo[x]:
      print("Yes")
    else:
      print("No")
    pass