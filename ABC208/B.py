# https://atcoder.jp/contests/abc208/tasks/abc208_b


# p円払いたい
# 1.大きいものから払っていく
from math import factorial
p = int(input())

answer = 0

for i in range(10,0,-1):
  while(factorial(i) <=p):
    answer += 1
    p -= factorial[i]
print(answer)

