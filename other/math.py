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
# 参考一部　https://note.nkmk.me/python-math-factorial-permutations-combinations/

# N個のものを並べる  N! 



def kaijo(N:int):
    ans = 1
    for i in range(N):
        ans *= i+1

    return ans

# mathのfactorialを使う場合
import math
math.factorial(5)


print(kaijo(5)) # -> 120


#順列 
# N個のものをr個並べる　nPr　 
# p = N! / (N - r)!

# 例 5個のものを3個並べる
import math
N = 5
r = 3
p =  math.factorial(N) / math.factorial(N - r)



# 文字の組み合わせ

import itertools
n = ['1', '2', '3', '4']
# p = itertools.permutations(n, r)  -> n個のものをr個並べる

#n個のものを2個並べる
# 書き方1 
for s in itertools.permutations(n, 2):
    print(s)
# -> ('1', '2')('1', '3') ...... ('3', '4')

# 書き方2　基本的にはこっちの方が便利
p_list = list(itertools.permutations(n, 2))
print(p_list) 
# ->[('1', '2'), ('1', '3'),......('3', '4')]




# 組み合わせ-----------

#  N個のものをr個選ぶ　nCr
# 例 5個のものを3個選ぶ
# c = n! / (r! * (n - r)!)

import math
N = 5
r = 3
c = math.factorial(N) // (math.factorial(N - r) * math.factorial(r))
    

# 4C2 の場合
for s in itertools.combinations(n, 2):
    print(s)  #->('1', '2') ,('1', '3')....

n = ['1', '2', '3', '4']
c_list = list(itertools.combinations(n, 2))
# ->[('1', '2'), ('1', '3'),......('3', '4')]



# 四捨五入
def round_off(n, digit=0):
    k = 10 ** digit
    return (n * k * 2 + 1) // 2 / p
            

round_off(12.5)       # ->  13.0
int(round_off(12.5))  # ->  13


# ソート
A = [2,4,1,3,5]
A.sort() # -> [1,2,3,4,5] 
A.sort(reverse=True) # -> [5,4,3,2,1] 

# 二次元配列のソート

A = [ [5,6] , [3,4] , [1,2]]
A = sorted(A,key=lambda x: x[1])
print(A) # -> [ [1,2] , [3,4] , [5,6] ]




# 配列の要素重複を取り除く
# https://atcoder.jp/contests/abc154/tasks/abc154_c 
A = [1,2,2,3,4,5,5,6]
set(A) # -> [1,2,3,4,5,6]

A = ["a","b","c","c"]
set(A) # -> ["a","b","c"]