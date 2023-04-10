# https://atcoder.jp/contests/atc001/tasks/unionfind_a
# Union-Find 木
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

	

n,m = map(int,input().split())
uf = unionfind(n)
for i in range(m):
	t, u, v = map(int, input().split())

	if t == 0:
		uf.unite(u,v)
	if t == 1:
		if uf.same(u,v):
			print("Yes")
		else:
			print("No")
    
  
 