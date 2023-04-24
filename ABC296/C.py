n,x = map(int,input().split())
A = list(map(int,input().split()))

# 6 5
# 3 1 4 1 5 9
# N = 10^5
# 113459 


s = set(A)
# print(s)
for i in range(n):
    # A[i] - A[j] == x
    # (1) A[i] - x == A[j] 
    #     A[i] - x　が Aの中に含まれてればok

    if A[i] - x in s:
        print("Yes")
        exit()  

print("No")

# 含まれているか問題はsetを使う  
