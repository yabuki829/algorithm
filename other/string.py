#文字列操作系




# 回転して同じ文字になるかどうか

def rotate(str,n):
  str[n:len(str)] + str[:n]

N = "ABC"
T = "CAB"
for i in range(len(N)):
  if T == rotate(N,i):
    print("同じ文字")
    break




N = int(input())

a = list(map(int, input().split()))

sum = sum(a)
ans = 0
for i in range(N):
  ans = N % a[i]

print(ans)


