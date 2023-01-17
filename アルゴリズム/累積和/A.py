# 累積和　いもす法

# 10 5
# 8 6 9 1 2 1 10 100 1000 10000
# 2 3
# 1 4
# 3 9
# 6 8
# 1 10

# 売上
# 8 6 9 1 2 1 10 100 1000 10000
# 売上の累計
# 1日目は8,2日目は14,3日目は23
# 8 14 23 ..... X


# L日目からR日目までの売上を求めるには 
# * R日目までの売上 - L-1日目までの売上

N,Q = map(int,input().split())
A = list(map(int,input().split()))

L = [ None ] * Q
R = [ None ] * Q

for i in range(Q):
  L[i],R[i] = map(int,input().split())
  
# -- 累積和の計算--
S = [None] * (N+1)
# １日目の売り上げは0円
S[0] = 0

for i in range(N):
  S[i+1] = S[i] + A[i]
# --------------
for i in range(Q):
  r = S[R[i]]
  l = S[L[i] - 1]
  
  print(r-l)

# ----------------------------------------------------

def solve():
  N = int(input())
  A = list(map(int,input().split()))
  Q = int(input())

  L = [None] * Q
  R = [None] * Q

  # 累積和実装する
  atari  = [0] * (N+1)
  hazure = [0] * (N+1)

  for i in range(N):
    atari[i+1] = atari[i]
    hazure[i+1] = hazure[i] 
    if A[i] == 1:
      atari[i+1] +=1
    else:
      hazure[i+1] += 1

  for i in range(Q):
    L[i],R[i] = map(int,input().split())


  # 結果を表示する
  for i in range(Q):
    l,r = L[i],R[i]
    
    if atari[r] - atari[l-1] > hazure[r] - hazure[l-1]:
      print("win")
    elif atari[r] - atari[l-1] < hazure[r] - hazure[l-1]:
      print("lose")
    else:
      print("draw")

solve()


# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g

# Event Attendance [C]

def solve2():
  # 8日
  # 5人
  # 2 3
  # 3 6
  # 5 7
  # 3 7
  # 1 5

  D = int(input())
  N = int(input())
  L = [None] * N
  R = [None] * N

  for i in range(N):
    L[i],R[i] = map(int,input().split())

  #前日との差のデータを作成
  S = [0] * (D+2) # +2 は開始日と終了日
  for i in range(N):
    S[L[i]] += 1
    S[R[i] + 1] -= 1

  # 累積和
  Answer = [0] * (D+2)
  for i in range(1,D+1):
    Answer[i] = Answer[i-1] + S[i]
  
  # 結果を出力
  for i in range(1,D+1):
    print(Answer[i])



solve2()
  

# ----------------------------------
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
def solve3():

  T = int(input())
  N = int(input())
  L = [None] * N
  R = [None] * N
  for i in range(N):
    L[i],R[i] = map(int,input().split())
  
  #従業員比の差のデータ作成
  data = [0] * (T+1)
  for i in range(N):
    data[L[i]] += 1
    # data[R[i]] -= 1でも動く 
    data[R[i-1]] -= 1

  
  Answer = [0] * (T+1)
  # 開始時刻の人数を代入しておく
  Answer[0] = data[0]
  for i in range(1,T+1):
    Answer[i] = Answer[i-1] + data[i]
  

  for i in range(T):
    print(Answer[i])
 

solve3()