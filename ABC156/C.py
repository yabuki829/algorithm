# https://atcoder.jp/contests/abc156/tasks/abc156_c

# 問題
# (1).N人住んでいる
# (2).i番目の人が住んでいる座標Xi
# (3).i番目の人が集会に参加するためのコスト(Xi - P)^2

n = int(input())
X = list(map(int,input().split()))

# 考察
# 制約はXi<100なので100パターン調べる


def solve():
  ans =  1000000
  X.sort()
  for p in range(1,100):
    total = 0
    for x in X:
      total += (x - p)**2
    ans = min(ans,total)

  return ans
print(solve())



