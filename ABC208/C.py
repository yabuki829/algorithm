# https://atcoder.jp/contests/abc208/tasks/abc208_c
# n= 国民の数
# k= お菓子の数
n,k = map(int,input().split())
a = list(map(int,input().split()))

# 動作
# 1. お菓子の数がN個以上であれば全員に1個ずつお菓子を配る
# 2. N以下であれば,残りの数をkと置き、Aの小さい方から1個ずつお菓子を配る

# 終わったときA[i]番目の人のお菓子の数

# 一人当たりのお菓子の数
okasi_one = k // n
# 配った後のお菓子の個数
k = k % n

kokumin = []

for i in range(n):
  # [0]に国民id , [1]元の位置, [2]お菓子の数 
  kokumin.append([ a[i],i ,okasi_one])

# 国民idでソートする
kokumin.sort()
# print(kokumin)


for i in range(k):
  # 残りのお菓子を配る
  kokumin[i][2] += 1 

# 元の順番でソートする
kokumin.sort(key=lambda x:x[1])

for i in range(n):
  print(kokumin[i][2])