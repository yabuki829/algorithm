

from itertools import product
A = [1, 2, 3, 4]
n = len(A)
for bits in product([0, 1], repeat=n):
    select = []
    # print("bits: ", bits)
    
    for i in range(len(A)):
      if bits[i] == 0:
        select.append(A[i])
    
    print(select)


# https://atcoder.jp/contests/abc128/tasks/abc128_c

# N個のスイッチ
# M個の電球

# 電球iはKiこのスイッチにつながっている
# スイッチがオンになっている数を2で割った余がPiに等しい時に点灯する
from itertools import product

N,M = map(int,input().split())
S = []
for _ in range(M):
  s = list(map(int,input().split()))
  # 0番目を除く
  S.append(s[1:])
P = list(map(int,input().split()))
ans = 0

for bits in product([0, 1], repeat=N):
  # 電球がついているかどうか 0 ならon
  check = [False] * M
  # 電球の選択 i 
  for i in range(M):
    # オンにしたスイッチの数
    on_cnt = 0
    # スイッチを選択 j 
    for j in range(N):
      # スイッチがオンである かつ　スイッチのが接続されているか (j+1 が S[j]番目に含まれているか)
      if bits[j] == 1 and j + 1 in S[i]:
          on_cnt += 1

    if on_cnt % 2 == P[i]:
      check[i] = True
    else:
      check[i] = False

  # 全電球が付いている状態
  if all(check):
    ans += 1

    
print(ans)