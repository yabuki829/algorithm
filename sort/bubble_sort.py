# 計算量は，O(n2)

# 右側から完成していく

import random
def bubble_sort(data):
  change = True   #交換の余地ありと仮定

  for i in range(len(data)):
    print(data)
    if not change: 
      break
    change = False  # falseのままだとソートが完了

    for j in range(len(data) - i - 1):
      if data[j] > data[j+1]: #左の方が大きい場合
          #入れ替える
        data[j], data[j+1] = data[j+1], data[j] 
        change = True 

  return data


data = [40, 70, 60, 90, 20, 80, 30, 10, 50]
random.shuffle(data)

print(bubble_sort(data))