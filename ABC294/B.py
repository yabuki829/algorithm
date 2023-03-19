h,w = map(int,input().split())
A = [list(map(int, input().split())) for i in range(h)]

s = [[""]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
    if A[i][j] == 0:
      s[i][j] = "." 
    else:
      ord('A')
      s[i][j] = chr(A[i][j]+64).upper()



for i in range(h):
  for j in range(w):
    print(s[i][j],end="")
  print()




# elif n < m:
#   for i in range(10*6):
#     if len(A) == 0:
#       isA == True
#       break
#     if len(B) == 0:
#       isA = False
#       break
  
#     cnt += 1
#     if A[0] < B[0]:
      
#       ans_a.append(cnt)
#       A.pop(0)
#     else:
#       ans_b.append(cnt)
#       B.pop(0)