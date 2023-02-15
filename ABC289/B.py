# レ点の問題　難しい

# https://atcoder.jp/contests/abc289/tasks/abc289_b

# unionfindを使う
# 5 3
# 1 3 4

class unionfind:
    # 親
    p = []
    # 深さ
    r = []
    # 頂点の数
    n = 0

    def __init__(self, n):
        self.n = n
        # 最初は親がいないので,-1入れておく
        self.p = [-1] * (n)
        self.r = [1] * (n)

    # xの親を返す
    def find(self, x):
        # 自分が親であればxを返す
        if self.p[x] == -1:
            return x
        else:
            # 親要素を辿る
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    # 結合する
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # x,yが同じ親を持っていれば統合しない

        if x == y:
            return
        # 大きい数字を親にしたい
        if x>y:
            x,y=y,x
        self.p[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
uf = unionfind(n)

A=[int(a) for a in input().split()]

for i in A:
    uf.unite(i-1, i)

# 数字が読まれたかどうか
ok = [False] * (n+1)
# 読む順番
answer = []


for i in range(n):
  # print("-----------------",i+1,"の要素について考えます-----------------")
  if ok[i]:
    continue
  # 後ろにレ点がある
  if uf.p[i] == -1 :
    # print(i+1,"を追加します")
    answer.append(i+1)
  
  else:
    x = uf.find(i)
    # print(i+1,"の親要素は",x+1)
    for j in range(x,i-1,-1):
      # print(j+1,"を追加します")
      answer.append(j+1)
      ok[j] = True
   
    
# print(uf.p)
print(*answer)
