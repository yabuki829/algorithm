n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
A.sort()
B.sort()
# print(A)
# print(B)
 
import bisect 
min_ans = float('inf')
 
 
for i in range(n):
  # print("-------------")
  # print(i+1,"人の人が売ってもいいと考えています")
  
  index = bisect.bisect_right(B,A[i])
 
  # print(len(B[index:]),"人が購入しても良いと考えてます")
  if i+1 >= len(B[index:]):
    min_ans = min(min_ans,A[i])
    if index == m:
      min_ans = B[-1]+1
    
    break
 
print(min_ans)