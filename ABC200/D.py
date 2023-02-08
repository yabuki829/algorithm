# https://atcoder.jp/contests/abc200/tasks/abc200_d

# https://www.youtube.com/watch?v=y7LtMbF4lzQ
# https://qiita.com/u2dayo/items/c46a42346a7301af64b4#c%E5%95%8F%E9%A1%8Cringos-favorite-numbers-2
# 5
# 180 186 189 191 218

# BとCは異なる数列 
# A[B数列] % 200 == A[C数列] % 200
n = int(input())
A = list(map(int,input().split()))

# 考察
# 一個以上の数列選び方 2^n - 1

# 200で割った余りの範囲は 1~199の200通りある
# つまり 2^n -1 > 200   
# n>=8 (255>200)であれば 当然一致するあまりがある。(鳩の巣原理)
# 配列の前から8個で事足りる

# data[あまり] -> あまりになる選び方を入れる
data = [[] for _ in range(200)]

if n > 8:
  A = A[:8]

M = len(A)

for bit in range(1,2**M):
  # 合計
  sum = 0
  # 選択した要素
  selected = []
  for i in range(M):
    # 1の時にしたい処理を書く
    if (bit >> i) & 1:
      sum += A[i]
      selected.append(i+1)

  sum_amari = sum % 200

  data[sum_amari].append(selected)



# 1 <= k<= 199 のあまり kが2個以上のやつを探す
for i in range(200):
  if len(data[i]) >= 2:
    B = data[i][0]
    C = data[i][1] 
    print("Yes")
    print(len(B),*B)
    print(len(C),*C)
    exit()

print("No")
