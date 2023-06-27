n = int(input())
A = list(map(int,input().split()))


count = [0] * (n + 1)

ans = []

# print(A)
for i in range(n*3):
  count[A[i]] += 1
  if count[A[i]] == 2:
    ans.append(A[i])

  if len(ans) == n:
    break

print(*ans)

# 通った
# たまたま？
