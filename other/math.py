#配列の中身を合計する　*試してないけど一次元配列でしか使えない

A = [1,2,3]
S = sum(A) # -> 6


#ユークリッドの互除法

# やり方
# 【step1】: aをbで割り，あまりrを求める
# 【step2】: a, bをb, rでそれぞれ置き換える
# 【step3】: あまりrが0なら，その時の割る数bが最大公約数で，そうでなければstep1へ戻る


def gcd(a, b):
    r = a % b
    #あまりが0でなければ続ける
    while r != 0:
        a, b = b    , r
        r = a % b

    return b

num1 = 100
num2 = 25
# Greatest Common Diviso 最大公約数
GCD = gcd(num1, num2)

print(GCD)


# フィボナッチ数列

def fibo(N):
    a, b = 0, 1
    while b < N:
        print(b," ", end='')
        a, b = b, a+b
#　四桁目まで値を返す
fibo(4)

# N桁目の数字を返す
def fibo(N):
    a, b = 0, 1
    while b < N:
        print(b," ", end='')
        a, b = b, a+b
    return a


print(fibo(4))


# 素数判定
# エラトステレスのふるい
# 整数Nが素数かどうかは,
# Nが√Nまでの整数で割り切れるかどうかで判定ができる


#例)  47が素数かどうか
# √36 < √47 < √49 -> つまり　6 < √47 < 7
# √47 = 6.. 
# 2 ~ 6までの整数で割り切れなければ　"素数"　

import math
def isPrime_Number(N:int):
    n = math.floor(math.sqrt(N))
    result = True
    for i in range(n-2):
      if N % (i+2) == 0:
        #割り切れたら素数じゃない
        result = False
        break

    return result
    
print(isPrime_Number(47))


# 場合の数

# N個のものを並べる  N! 
def kaijo(N:int):
    ans = 1
    for i in range(N):
        ans *= i+1

    return ans


print(kaijo(5)) # -> 120


# N個のものをr個並べる　nPr　


# N個のものをr個選ぶ　nCr
    









