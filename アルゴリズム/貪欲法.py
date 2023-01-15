# 一手先の最適化は貪欲法

# 一手先では最適ではないが将来的に最適になる選択を切り捨てる可能性がある


# (a) 交換しても悪化しない
# (b) 現在が良いほど未来も良い


# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b
# 区間スケジュール問題

N = int(input())

# s[i][0] -> 仕事の開始時刻
# s[i][1] -> 仕事の終了時刻
s = [list(map(int, input().split())) for i in range(N)]
  
s = sorted(s,key=lambda x: x[1])

#何個の仕事を受けれるか
count = 0
#現在の時刻
now = 0
for i in range(N):
  # 現在の時刻より仕事の開始時刻の方が大きければ仕事を受ける
  if s[i][0] > now:
    count += 1
    now = s[i][1]
    
print(count)