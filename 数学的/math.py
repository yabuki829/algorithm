#配列の中身を合計する　*試してないけど一次元配列でしか使えない

A = [1,2,3]
S = sum(A) # -> 6


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

n = 5
for i in range(n):
  for j in range(i,n):
    print(i,j)
# (0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(1,2)....(4,4)


# 組み合わせ-----------


#  N個のものをr個選ぶ　nCr
# 例 5個のものを3個選ぶ
# c = n! / (r! * (n - r)!)

import math
n = 5
r = 3
c = math.factorial(N) // (math.factorial(N - r) * math.factorial(r))

import math
def comb(n,r):
  return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))


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
set(A) # -> {1, 2, 3, 4, 5, 6}

A = ["a","b","c","c"]
list(set(A)) # -> ["a","b","c"]

# 約数列挙 O(√N)で使える
#参考記事 https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            print("割り切れた場合")
            lower_divisors.append(i)
            if i != n // i:
                print("i=",i,"がn//i=",n//2,"と同じでない場合")
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

make_divisors(2) # -> [1,2]

# 左回転90度回転
import numpy as np
# 入力
A = [[0,1,2],[3,4,5],[6,7,8]]
# NumPy配列への変換
# A = np.array(A)
print(np.rot90(A))

# 90度右回転
# 1. 上下逆転
# 2. 列と行の入れ替え
def rotete90(A):
  # print("回転します")
  A = A[::-1]
  routate_A = []
  for x in zip(*A):
    routate_A.append(x)
  return  routate_A
rotete90(A)

# 180度回転
# 1. 左右逆
# 2. 上下逆

def rotete180(A):
    routate_A = []
    for x in A[::-1]:
        print(x)
        routate_A.append(x)
    return routate_A
    



