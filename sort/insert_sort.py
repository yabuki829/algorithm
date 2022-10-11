import random

def insert_sort(data):
    for i in range(1, len(data)):
      #挿入データを一時的に記録
        temporary = data[i]
        #j番目までソートが完了している         
        j = i - 1

         #挿入データがソート済みデータ内のデータよりも小さく右にあれば繰り返し入れ替え
        while (j >= 0) and (data[j] > temporary):  
            data[j + 1] = data[j]       #右へ1つデータを移す
            j -= 1
        data[j + 1] = temporary     #上の操作で移動を終えた所に一時的に記録していた挿入データを代入

    return data


data = [40, 70, 60, 90, 20, 80, 30, 10, 50]
random.shuffle(data)


print(insert_sort(data))