# https://atcoder.jp/contests/abc294/tasks/abc294_d

# 呼ばれた人 
Called = {}

# 次の客
customer = 1
n, q = map(int,input().split())

for i in range(q):
  event = list(map(int,input().split()))
  
  if event[0] == 1:
    Called[customer] = 1
    customer += 1

  elif event[0] == 2:
    Called.pop(event[1])
  else:
    print(next(iter(Called)))



# データの持ち方 辞書