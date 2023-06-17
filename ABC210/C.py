# https://atcoder.jp/contests/abc210/tasks/abc210_c
N,K = map(int,input().split())

C = list(map(int,input().split()))
# 制約
# 1 <= K <= N <= 3*10^5
# (n - k) + 1
# Nが最大値,Kが最小値の場合telになる

# max_ans = 0

# for i in range(N - K + 1):
#   c = C[i:i+K]
#   count = len(set(c))
#   max_ans = max(max_ans,count)

# print(max_ans)


# キャンディの順番
# 1 2 1 2 3 3 1

# O(N)で行ける
# 一番前を取り除き、一番後ろに新しいキャンディを入れる
# ( 1 2 1 ) 2 3 3 1 ->  Counter({1: 2, 2: 1})
# 1 ( 2 1 2 ) 3 3 1 ->  Counter({2: 2, 1: 1})
# 1 2 ( 1 2 3 ) 3 1 ->  Counter({1: 1, 2: 1, 3: 1})

from collections import Counter
counter = Counter(C[:K])
max_ans = len(counter)

for i in range(K,N):
  # Kからスタートするので最初はleft = C[0]になる
  # print(counter)
  left = C[i - K]
  right = C[i]
  counter[left] -= 1
  counter[right] += 1 

  if counter[left] == 0:
    del counter[left]
  max_ans = max(max_ans,len(counter))




# 理解度C
# これは初見ではまだ思いつかんわ