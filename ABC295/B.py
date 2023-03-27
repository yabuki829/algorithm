R,C = map(int,input().split())


B = []


# 爆弾の威力, x, y
bakedan_list = []
for i in range(R):
  s = input()
  B.append([i for i in s])

bakedan_list.sort()

for i in range(R):
  for j in range(C):
    if B[i][j] != "#" and B[i][j] != ".":
      bakedan_list.append([int(B[i][j]),i,j])



for b in bakedan_list:
  power,r,c = b
  # 爆弾のますを . に変更する
  B[r][c] = "."
  for i in range(-power, power+1):
        for j in range(-power, power+1):
          # 爆風が届く範囲のマスを処理
          if abs(i) + abs(j) <= power: 
                nr, nc = r+i, c+j
                # はみ出ないかどうか判別
                if 0 <= nr < R and 0 <= nc < C:
                    B[nr][nc] = "." 


for b in B:
  print(*b,sep='')
