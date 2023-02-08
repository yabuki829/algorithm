# https://atcoder.jp/contests/abc200/tasks/abc200_c

# Ringo's Favorite Numbers 2

# 1≤i<j≤N
# Ai - Aj = 200の倍数


# 6
# 123 223 123 523 200 2000

n = int(input())
A = list(map(int,input().split()))

# A[i]を200で割ったあまり == A[j]を200で割ったあまり


# Aを200で割った余りの配列を作成する(mod200)
# 範囲は200で割った余りなので1~199になる
new_A = [x % 200 for x in A]
# 今回の場合 
# print(new_A) -> [123, 23, 123, 123, 0, 0] になる

# 何が何回でできたか数える
count = [0] * 200 

ans = 0
for a in new_A:
  # 1の時はanswerに入れない. 1C2 = 0
  # 2の時は2C2 = 1
  # 3の時は3C2 = 3
  ans += count[a]
  count[a] += 1
  
print(ans)
