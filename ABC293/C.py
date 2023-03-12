h,w = map(int,input().split())
A = [list(map(int, input().split())) for i in range(h)]

# ゴールの数
ans = 0
visited = set()

def dfs(x,y,visited):
  global ans
  visited.add((x,y))
  # ゴールしたとき
  if x == h-1 and y == w-1:
    nums = set()
    # 通ったところを確認する
    # set関数で通ったところの数字を保存する
    # 保存した数字の数がh+w-1であればタカシくんは嬉しくなる
    for x2 ,y2 in visited:
      # 座標(x2,y2)の数字
      a = A[x2][y2]
      nums.add(a)
      
    if len(nums) == h+w-1:
      ans+=1

  else:
    # 右が壁でないか,訪れた場所でないか
    if x+1 <=w and (x+1,y) not in visited:
      dfs(x+1,y,visited)

    # 下が壁でないか,訪れた場所でないかどうか
    if y+1 <=h and (x,y+1) not in visited:
      dfs(x,y+1,visited)
  
  visited.remove((x, y))

dfs(0, 0, visited)
print(ans)

# 1回目解けなかった。


# 再帰　bit全探索 dfs
