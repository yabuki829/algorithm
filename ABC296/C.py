n,x = map(int,input().split())
A = list(map(int,input().split()))

# 6 5
# 3 1 4 1 5 9


# N = 10^5

# 113459 
 
# 13459

s = set(A)

for i in range(n):
    if A[i] - x in s:
        print("Yes")
        exit()

print("No")