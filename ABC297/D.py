A, B = map(int, input().split())

# A = 100
# B = 20
def gcd(a, b):
    r = a % b
    #あまりが0でなければ続ける
    while r != 0:
        a, b = b    , r
        r = a % b
    print(r)
    return b



# g = gcd(A,B)
# print(g)
# A /= g
# B /= g

# A>Bならば　A = A−B
# A<Bならば　B = B-A

# A==Bで終了
# 制約1≤A,B≤10**18
cnt = 0
while(A!=B):
  if A > B :
    A -= B
  else:
    B -= A
  cnt += 1

print(cnt)

# 溶けてない



