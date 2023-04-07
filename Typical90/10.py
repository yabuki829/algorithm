# https://atcoder.jp/contests/typical90/tasks/typical90_j

# 累積和かな？

n = int(input())

# クラスは C<=2
#  0番目は1組 1番目は二組


class_1 = [0] * (n+1)
class_2 = [0] * (n+1)

for i in range(n):
  c,p = map(int,input().split())
  if c == 1:
    class_1[i+1] = class_1[i] + p
    class_2[i+1] = class_2[i]
  else:
    class_2[i+1] = class_2[i] + p
    class_1[i+1] = class_1[i] 

q = int(input())
for _ in range(q):
  l,r = map(int,input().split())
  a = class_1[r] - class_1[l-1]
  b = class_2[r] - class_2[l-1]
  print(a,b )
  # 1組のL~Rまでの生徒の合計
  # 2組のL~Rまでの生徒の合計
  pass

# 累積和