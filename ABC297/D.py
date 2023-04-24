A, B = map(int, input().split())


# A>Bならば　A = A−B
# A<Bならば　B = B-A
# 制約1≤A,B≤10**18

# 3 8

# 1. Bの方がでかい
#    b = b - a  + 1
#    3 5
# 2. B の方がでかい
#    b = b - a + 1
#    3 2
# 3. Aの方がでかい
#    a = a - b + 1
#    1 2
# 4. Bの方がでかい
#    b = b - a + 1
#    1 1 
# 終了 

cnt = 0
while(A != 0 and B != 0):
  if A == 0 or B == 0:
    break
  if A > B:
    # あまりを入れる
    cnt += A//B
    A = A%B 
  else:
    cnt += B//A 
    B = B%A
    



print(cnt-1)