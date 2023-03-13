# https://atcoder.jp/contests/abc208/tasks/abc208_c
# n= 国民の数
# k= お菓子の数
n,k = map(int,input().split())
a = list(map(int,input().split()))

# 動作
# 1. お菓子の数がN個以上であれば全員に1個ずつお菓子を配る
# 2. N以下であれば,残りの数をkと置き、Aの小さい方から1個ずつお菓子を配る

# 終わったときA[i]番目の人のお菓子の数

