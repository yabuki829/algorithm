# 貪欲法

#　https://atcoder.jp/contests/abc131/tasks/abc131_d
# 締め切りまでにN件のしごとを終わらせることはできますか？
# 締め切りでソートして順番にやっていく
N = int(input())

schedule = []
# Aがかかる時間
# Bが締め切り

now = 0
for _ in range(N):
  A,B = map(int,input().split())
  schedule.append([B,A])

# 締め切りの順番で仕事をしていくだけでは、締め切りに間に合わない場合があるかも

schedule.sort()

for i in range(N):
  b,a = schedule[i]
  now += a
  if now > b:
    print("No")
    exit()

print("Yes")

# 簡単すぎ？
# 理解度A