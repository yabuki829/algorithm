# https://atcoder.jp/contests/abc207/tasks/abc207_b
# 5 2 3 2

a,b,c,d = map(int,input().split())
# x回操作した
# A+Bx =< D*Cx 
# A =< D*Cx-Bx

t = d*c-b
if t<=0:
  print(-1)
else:
  
  print(-(-a//t))



# 全探索で解く
a,b,c,d = map(int,input().split())

limit = 10**7
for x in range(limit):
  blue = a + b * x
  red = c*x*d
  if blue <= red:
    print(x)
    exit()
print(-1)

  

# 数学的、全探索

