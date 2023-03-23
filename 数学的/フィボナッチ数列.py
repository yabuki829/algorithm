
# フィボナッチ数列の一般頂
# An = 1/√5( (1+√5 / 2)^n - (1-√5/2)^n )

# フィボナッチ数列
def fibo(N):
  a, b = 0, 1
  array = []
  while N:
    N-=1
    array.append(b)
    a,b = b, a+b
    
  return array

print(fibo(10)) # -> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# N桁目の数字を返す
def fobo(N):
    a,b = 0,1
    while N-1: 
        N-=1
        a,b = b,a+b
    
    return b

print(fibo(10)) # -> 89




# トリボナッチ数列

# 0 0 1 1 2 4 7 13 ....
