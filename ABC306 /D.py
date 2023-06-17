n = int(input())
xy = []
for i in range(n):
  xy.append(list(map(int,input().split())))
print(xy)
isPoizen = False
dp = [0] *  (n+1)
print(dp)

# 2^N - 1