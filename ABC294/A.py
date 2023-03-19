# 5
# 1 2 3 5 6

N = int(input())
A = list(map(int,input().split()))
ans = []
for a in A:
  if a % 2 == 0:
    ans.append(a)

print(*ans)