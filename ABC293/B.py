k = int(input())
A = list(map(int,input().split()))

isCalled = [False] * k


for i in range(k):
  if isCalled[i] == False:
    isCalled[A[i]-1] = True

print(isCalled)
ans = []
cnt = 0
for i in range(k):
  if isCalled[i] == False:
    ans.append(i+1)
    
print(len(ans))
print(*ans)

