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