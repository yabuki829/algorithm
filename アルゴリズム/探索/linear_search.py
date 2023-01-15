#線形探索
#前から順番に探していく
#データはソートする必要なし

def linear_search(data, value:int):

  for i in range(len(data)):
    if data[i] == value: 
      return i

  return -1


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(linear_search(data,90))


#組み合わせの最小値,最大値を調べる
min = 10000
max = -1
for i in range(len(data)):
  for j in range(len(data)):
    # 最小値
    if min > data[i] + data[j]:
      min = data[i] + data[j]

    if max < data[i] + data[j]:
      max = data[i] + data[j]

print("最小値",min)
print("最大値",max)


