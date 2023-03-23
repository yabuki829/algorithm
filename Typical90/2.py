# https://atcoder.jp/contests/typical90/tasks/typical90_b


# 制約　
# 1 <= N <= 20

# a. ビット全探索をする O(2^n)
#   1 = "(" 
#   0 = ")"   

# b. 組み合わせの中で  正しいカッコ列かどうかを判別する O(N)
def ok(S:str):
  score = 0

  for i in range(len(S)):
    if S[i] == "(":
      score += 1
    else:
      score -= 1

    # scoreがマイナスになれば必ず正しくないカッコ列 
    if score < 0:
      return False

  return score == 0

N = int(input())

from itertools import product

for S in product(['(', ')'], repeat=N):
  if ok(S):
    print(*S,sep="")

# 星3 400 ～ 799
# bit全探索
# 参考
# https://drken1215.hatenablog.com/entry/2021/06/12/151200