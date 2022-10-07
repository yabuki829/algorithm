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