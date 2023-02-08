# 2 2


A,B = map(int,input().split())


# N * (8 / 100) = a
# N * (10 / 100) = a

#　＜全探索できないかまず考える＞
# 今回の場合探索範囲は 消費税が100円までなので 元の金額は10000円を超えることはない。つまりN=10000で　10^5なので全探索が可能
import math
for i in  range(10000):
  a = math.floor(i * 8 / 100 )
  b = math.floor(i * 10 / 100 )

  if a == A and b == B :
    print(i)
    exit()

print(-1)