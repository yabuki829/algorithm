# https://atcoder.jp/contests/atc001/tasks/dfs_a

# 4 4
# ...s
# ....
# ....
# .g..
# 検索中にゴールが出てきたら終了

h,w = map(int,input().split())
visited = [[False for j in range(w)] for i in range(h)] 

# 迷路
s = []
for i in range(h):
  s.append(input())
sy = 0
sx = 0
# スタート地点を探す
for i in range(h):
  for j in range(w):
    if s[i][j] == "s":
      # スタート地点
      sy,sx = i,j
      break
      

S = list() 

S.append((sy,sx))
goal = False
while len(S) >= 1:
  # 現在地を
  y,x = S.pop()
  #print("現在地",y,x)
    
  if s[y][x] == "g":
    goal = True
    break
    
  if visited[y][x]:
    continue
    
  if s[y][x] == "#":
    continue
    
  visited[y][x] = True

  # 次の座標が枠外でないか判別
  if y-1>=0:
    S.append((y-1,x)) #上
  if y+1<h:
    S.append((y+1,x)) #下

  if x+1<x:
    S.append((y,x+1)) #右

  if x-1>=0:
   S.append((y,x-1)) #左
       

  
if goal:
  print("Yes")
else:
  print("No")
  
  
  
  
    
  
   
  
