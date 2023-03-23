# https://atcoder.jp/contests/typical90/tasks/typical90_a

N,L = map(int,input().split())
K = int(input())
A = list(map(int, input().split()))

# 最小値Xにピースを分割したときにピースの数がK子以上になるか


# 最小値がxだった場合ピースはk子以上になるか
# 他のピースも全てx以上であるか

def nibuntansaku(x):
  # print("-----------------------------")
  # print("切れ目の最小値が",x,"だった場合")
  # print("-----------------------------")
  # 最後に切った切れ目の長さ
  currnet = 0
  # 現在のピースの数
  pieces = 0
  
  for i in range(N):
    if A[i] - currnet >= x:
      # print(i+1,"個目の切れ目できれば",x,"を超えます")
      # print(A[i],"-",currnet, A[i] - currnet)
      pieces += 1
      currnet = A[i]
    else:
      # print(i+1,"(",A[i] - currnet,")","コメの切れ目で切ると",x,"を超えません")
      pass

  if L - currnet >= x:
    pieces += 1
  #   print(L - currnet,">=",x,"まだ切れるのでpieaceを増やします")
  # print("最終的なピースの数",pieces)


  return pieces



left, right = 0 , L
# 一番小さいピースがXの時 K+1個のピースを作れますか？
while right - left > 1:
  middle = (left + right) // 2 
  if nibuntansaku(middle) >= K + 1:
    # xセンチいじょうのピースを K+1 以上作れたということ
    # 最小値の値の範囲を増やす
    # print("最小値を右に動かします")
    left = middle
  else:
    # 最小値xセンチを満たす K+1の羊羹は作れない
    # print("最小値を左に動かします")
    right = middle
    


print(left)



# 二分探索

#星4 800~1199