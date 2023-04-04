# 深さ

# 3 3 h,w
# 0 0 スタート y,x
# 2 0 ゴール  y,x

# 123
# ##4
# ...


from collections import deque

h,w = map(int,input().split())
# スターとの座標
sy,sx = map(int,input().split())
# ゴールの座標
gy,gx = map(int,input().split())
# 訪れたかどうかを表す
visited = [[False for j in range(w)]for i in range (h)]
# 迷路
s = []
for i in range(h):
  s.append(input())

q = deque()
q.append((sy,sx,0))

ans = -1
while len(q) > 0:
  #　データを取り出す　
  y,x,step = q.popleft()
  
  # ゴールかどうか
  if y == gy and x == gx:
    ans = step
    break
  # 枠外でないかどうか
  if y < 0 or x < 0 or y >= h or x >= w:
    continue
  # 訪れた場所かどうか
  if visited[y][x]:
    continue
  visited[y][x] = True 

  # 現在の座標が壁でないかを調べる
  if s[y][x] == "#":
    continue
  
  q.append((y+1,x,step+1))#上
  q.append((y-1,x,step+1))#下
  q.append((y,x-1,step+1))#左
  q.append((y,x+1,step+1))#右
    


    
  