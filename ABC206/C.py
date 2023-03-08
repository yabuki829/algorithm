# https://atcoder.jp/contests/abc206/tasks/abc206_c
n = int(input())
A = list(map(int,input().split()))


# 20
# 7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4

cnt = {}
#  すべての選び方　- 同じ数の中から2個選ぶ通り数 
for e in A:
  # 値がなければ作成する
  if e not in cnt:
    cnt[e] = 0
  cnt[e] += 1

print(cnt)
def nC2(n):
  return n * (n-1) // 2

ans = nC2(n)
for e in cnt:
  ans -=nC2(cnt[e])

print(ans)

# 条件を逆から考える