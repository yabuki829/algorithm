
# データの中から最小値を探す
# 最小値と先頭の値を入れ替え最小値を整列済みデータとする
# 処理1～2を繰り返し、すべてのデータが整列済みになったら終了


def selection_sort(data):
  for i in range(len(data)):
    min = i
    for j in range(i+1,len(data)):
      if data[min] > data[j]:
        min = j
    
    data[i], data[min] = data[min], data[i]
  return data

data = [40, 70, 60, 90, 20, 80, 30, 10, 50]

print(selection_sort(data))