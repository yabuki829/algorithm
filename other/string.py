#文字列操作系




# 回転して同じ文字になるかどうか

def rotate(str,n):
  str[n:len(str)] + str[:n]

N = "ABC"
T = "CAB"
for i in range(len(N)):
  if T == rotate(N,i):
    print("同じ文字")
    break


# 配列の前からN番目から　後ろからM番目まで出力する 

# ls_s[( N-1 ):-( M-1 )]

ls_s = [1,2,3,4,5,6,7,8,9,10]
print(ls_s[1:-1])
# -> 2,3,4,5,6,7,8,9


# 文字列Sが配列の中にあるかどうか




