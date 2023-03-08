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

# 文字列のカウント
# 文字列にABCが含まれるか
S = "DFEABCDE"
print(S.count("ABC")) # -> 1



# 文字列を反転させる
S = "ABCDEF"
s_reverse = S[::-1] # -> FEDCBA

#  出現頻度を調べる
import collections
data = ["a","b","c","a"]

print(collections.Counter(data)) # -> Counter({'a': 2, 'b': 1, 'c': 1})
c = collections.Counter(data)
print(c["a"])  # -> 2