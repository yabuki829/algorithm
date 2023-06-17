A, B, C, D = map(int, input().split())

# A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数

# 考察1 
# 愚直な実装　全探索

# 4 ~ 9 のうちCでもDでも割り切れないもの
# 0~9　と 0~4を求める
# cとdで割り切れない数 = 全体　- C で割り切れる or Dで割り切れる - cとdで割り切れる
import math
def lcm(x, y): 
  return (x * y) // math.gcd(x, y)
def calc(x,C,D):
 # x - (cで割り切れる - Dで割り切れる　+ cとdで割り切れる)
  return x-(x//C)-(x//D)+(x//lcm(C,D))


def solve(A,B,C,D):
 
  return calc(B,C,D) - calc(A-1,C,D)
  
print(solve(A,B,C,D))


# 理解度B 
