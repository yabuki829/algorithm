N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(N):
      if A[i][j] == 1:
        if B[N-j][i] != 1 and B[i][j] != 1:
          print("No")
          exit()  
        else:
          A[i][j] = A[N-j][i]
print("Yes")