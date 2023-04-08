# https://atcoder.jp/contests/typical90/tasks/typical90_l


class unionfind:
	# 親
	parent = []
	# 深さ
	r = []
	# 頂点の数
	n = 0

	def __init__(self,n):
		self.n = n
		# 最初は親がいないので,-1入れておく
		self.parent = [-1] * (n+1)
		self.r = [-1] * (n+1)

	# xの親を返す
	def find(self,x):
		# 自分が親であればxを返す
		if self.parent[x] == -1 :return x
		else:
			# 親要素を辿る
			self.parent[x] = self.find(self.parent[x])
			return self.parent[x]

	# 結合する
	def unite(self,x,y):
		x = self.find(x)
		y  = self.find(y)

		# x,yが同じ親を持っていれば統合しない
		if x == y : return 
	 
		# <マージテク>集合をまとめる時に大きい方に小さい方を移動させることでマージさせる
		# xの深さとyの深さを比べている。
		if self.r[x] > self.r[y]:
			x,y = y,x
		# xとyのrankが同じ時にrankが上がる
		if self.r[x] == self.r[y]: 
			# yのrankを更新する　
			self.r[y] += 1
		
		# yの親要素をxに置き換えてます
		self.parent[x] = y
		self.n -= 1

	def same(self,x,y):
		return   self.find(x) == self.find(y)
	def size(self,x):
		return -self.parent[self.find(x)]


H,W = map(int,input().split())
Q = int(input())
# red = [[False] * (W) for _ in range(H)]
red = [[False] * (W+1) for _ in range(H+1)]
# 上右下左
dx = [0,1,0,-1]
dy = [1,0,-1,0]
uf = unionfind(H*W+1)

for i in range(Q):
  q = list(map(int,input().split()))
  if q[0] == 1:
    # r,cを赤色に塗る
    r,c = q[1],q[2]
    r -= 1
    c -= 1
    # 今回塗る座標を一次元の座標に変換したもの
   
    red[r][c] = True
    # 上下左右を確認して連結させる
    for i in range(4):
      new_r = r + dx[i] 
      new_c = c + dy[i]
      # 盤面外であればスキップ
      # redの範囲をw+1,h+1にすることで範囲外でなくなる
      # if new_r<0 or new_r>=H or new_c<0 or new_c>=W: continue
      if red[new_r][new_c] :
        # 二次元配列の座標を一次元に変換
        idx_1 = r*W + c
        idx_2 = new_r*W+new_c
        uf.unite(idx_1,idx_2)


  else: 
    a_r ,a_c = q[1],q[2]
    b_r ,b_c = q[3],q[4]
     
    a_r -= 1 
    a_c -= 1
    b_r -= 1
    b_c -= 1
    # 赤に塗られていなければno
    ok = True
    if red[a_r][a_c] == False or red[b_r][b_c] == False: ok = False 
    idx_1 = a_r * W + a_c
    idx_2 = b_r * W + b_c

    if uf.same(idx_1,idx_2) and ok:
      print("Yes")
    else:
      print("No")


# unionfind 連結かどうかの判別
# 一次元で二次元の情報を持つ