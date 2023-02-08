# https://atcoder.jp/contests/abc156/tasks/abc156_b

#　整数 N を K 進数で表したとき、何桁になるかを求めてください

n,k =  map(int, input().split())
ans = []

# 解き方
# nをkで何回割ることができるかを数える
while n > 0:
  n //= k
  ans.append(n%k)


print(len(ans)) 



#進数
