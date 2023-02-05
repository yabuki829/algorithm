# https://atcoder.jp/contests/atc001/tasks/unionfind_a
# Union-Find 木
class unionfind:
	# 親
	p = []
	# 頂点の数
	n = 0
	def __init__(self,n):
		self.n = n
		# 最初は親がいないので,-1入れておく
		self.p = [-1] * (n+1)

	# xの親を返す
	def find(self,x):
		# 自分が親であればxを返す
		if self.p[x] == -1 :return x
		else:
			# 親要素を辿る
			self.p[x] = self.find(self.p[x])
			return self.p[x]

	# 結合する
	def unite(self,x,y):
		x = self.find(x)
		y  = self.find(y)

		# x,yが同じ親を持っていなければ
		if x != y :
			# yの親要素をxに置き換えてます
			self.p[x] = y

	def same(self,x,y):
		return   self.find(x) == self.find(y)

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
    
  
 