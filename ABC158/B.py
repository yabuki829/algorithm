# 8 3 4
N,A,B = map(int,input().split())

# 青と赤の二色
# 列の末尾に、A 個の青いボールを加える。その後、列の末尾に B 個の赤いボールを加える。を 10 ^100 回繰り返します
 

# bbbrrrr

def solve():
  # bbbrrrr　が何個作れるか計算する
  
  count = N // (A+B) 
  # Aの個数
  A_count = count * A
  # bbbrrrr　をcount個作った時あまりのボールの数
  rem = N % (A+B) 
  # bbbrrrr
  # あまりのボールの数が
  # Aを超えていればAを足す 超えていなければremを足す

  # もしもあまりのボールの数が4であれば
  # bbbrが残っているということになる。
  # 青の数が答えなので,A と あまりのボールの数を比べて小さい方を足す
  #  
  ans = A_count + min(rem,A)
  print(ans)

solve()

