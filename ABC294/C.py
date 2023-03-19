



# ----------------------------------------
# 最大で　O(M+N) 
n,m = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))



ans_a = []
ans_b = []
cnt = 0
isA = False
for i in range(n+m):
    if len(A) == 0 :
      isA = True
      break
    if len(B) == 0:
      isA = False
      break

    cnt += 1
    if A[0] < B[0]:
      ans_a.append(cnt)
      A.pop(0)
    else:
      B.pop(0)
      ans_b.append(cnt)

if isA :
  for _ in range(len(B)):
    cnt+=1
    ans_b.append(cnt)
else:
  for _ in range(len(A)):
    cnt+=1
    ans_a.append(cnt)


    

print(*ans_a)
print(*ans_b)


# tel