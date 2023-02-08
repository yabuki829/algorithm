# https://atcoder.jp/contests/abc203/tasks/abc203_c

# 2 3
# 2 1
# 5 10

n, k = map(int,input().split())

# 1. 1円払うことで i+1に移動できる
# 2. 初めはK円持った状態でいる
# 3. N人の友達がいる
# 4. i人目の友達はA[i]番目のいる
# 5. A[i]番目に到着したら, B[i]円をもらう

A_B = []
for i in range(n):
  a,b = map(int,input().split())
  A_B.append([a,b])
A_B.sort()

# k円で行ける階層まで移動する
floor = k

for i in range(n):
  # 現在の階層が友達のいる階層より大きい場合,
  if floor >= A_B[i][0]:
    floor += A_B[i][1]
  else:
    break

print(floor)