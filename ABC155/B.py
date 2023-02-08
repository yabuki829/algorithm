N = int(input())

A = list(map(int,input().split()))


# 偶数であるものはすべて, 3 または 5 で割り切れる。
# つまり
# 偶数のものは,3と5で割り切れなければ,DENIED
isOk = True
for i in range(N):
  if A[i]%2 == 0 and (A[i]%3!=0 and A[i]%5!=0) :
    # print("3か5で割り切れない偶数です。",A[i])
    isOk = False
    break

if isOk:
  print("APPROVED")
else:
  print("DENIED")
    


# シフト＋コマンド+D