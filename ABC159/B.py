# S は回文である。
# N を S の長さとするとき、S の 1 文字目から (N−1)/2 文字目まで(両端含む)からなる文字列は回文である。
# S の (N+3)/2 文字目から N 文字目まで(両端含む)からなる文字列は回文である。


import math

def solve():
  S = input()
  n = len(S)

  # Sが怪文かどうか判定
 
  if S != "".join(reversed(S)):
    print("No",1)
    exit()
  #  1文字目~(n-1)/2 文字目までの文字列は回文であるか判定

  num_a = math.floor((n-1) /2)
  print(num_a)
  if S[0:num_a] !=  "".join(reversed(S[0:num_a])):
    print("No",2)
    exit()

  # (n+3)// 2文字目 ~ 最後までの文字列は回文であるか判定
  num_b = math.floor((n+3)/2) - 1
  
  if S[num_b:] !=  "".join(reversed( S[num_b:])):
     print("No",3)
     print(S[num_b:],"".join(reversed( S[num_b:])))
     exit()

  print("Yes")
   
    
solve()