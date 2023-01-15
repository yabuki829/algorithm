#二分探索

def binary_search(data, value):
  left = 0            
  right = len(data) - 1
  # 左側が左側より右に来たら終了
  while left <= right:
        mid = (left + right) // 2   
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        elif data[mid] > value:
            right = mid - 1
            
  return -1          

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))


#　N以上の値を求めるのにも使える