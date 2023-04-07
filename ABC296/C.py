n,x = map(int,input().split())
A = list(map(int,input().split()))

# 6 5
# 3 1 4 1 5 9
# N = 10^5
# 113459 


s = set(A)

for i in range(n):
    # A[i] - A[j] == x
    # A[i] - x == A[j] 
    if A[i] - x in s:
        print("Yes")
        exit()

print("No")