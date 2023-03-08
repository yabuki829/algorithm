# 素数判定
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


# エラトステネスの篩　------------------

# 計算量 ほぼO(N)らしい 実際には O(N log log N)

# 1. 最初に2~Nまでを用意する
# 2. 最小の値aを取り出し,aの倍数を全て削除する
# 3. 次にa以上の最小の値を取り出し,2の動作を繰り返す
# 4. √Nまで行けば終了し,残りの数字が素数

N = 50
DeletedNumber = [False] * (N+1)

M = int(N ** 0.5)

for  i in range(2,M):
  if DeletedNumber[i] == False: 
    # i^2 ~ N+1 までの中でiの倍数のものを探す
    print("-------------",i,"の倍数-------------")
    for j in range(i*2, N+1, i):
      print(j)
      DeletedNumber[j] = True


sosuu = []
for i in range(2,N+1):
  if DeletedNumber[i] == False:
    sosuu.append(i)
    
print(*sosuu)