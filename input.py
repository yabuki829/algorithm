#1つの文字列の入力
s = input()

#一つの整数の入力
N = int(input())


#一行に複数の文字列を入力
# s_1,s_2,s_3 

s = input().split()


#一行に複数の整数を入力
# i_1,i_2,i_3

  # pattern1 -> [_1,i_2,i_3]
i = list(map(int, input().split()))

  #pattern2
a, b, c = map(int, input().split())

#N行に一つの入力
# N
#s_1
#s_2
#s_3 
# -> [s_1,s_2,s_3]
N = int(input())

s = [input() for i in range(N)]
i = [int(input()) for i in range(N)]

#N行に複数の入力
# N
#s_1 i_1
#s_2 i_2
#s_3 i_3
# -> [[s_1,i_1],[s_2,i_2],[s_3,i_3]]
N = int(input())
data = [list(map(int, input().split())) for i in range(N)]


# 文字列をバラバラに配列に入れる
# apple -> ["a","p","p","l","e"]
ls = [s for s in input()]





