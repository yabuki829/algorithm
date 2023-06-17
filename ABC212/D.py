# https://atcoder.jp/contests/abc212/tasks/abc212_d

# たくさんのボールとからの袋を持っている
# 操作1 
# - 何も書かれていないボール一つに Xを書き込んで、袋に入れる
# 操作2
# - 袋に入っている全てのボールに書かれている数字にXを足す
# 操作3
# - 袋に入っているボールのうち最小のものを記録し,袋から取り出す

# 記録されたものを出力する
Q = int(input())


# Q <= 2*10^5
# 多分O(Q)でできる方法があるんかな？
# このコードは確実にtelする

# 操作2のx足すのは後回しにしてバッグから取り出すときにタス説？
bag = []
ans = []
for i in range(Q):
  query = list(map(int,input().split()))
  
  if query[0] == 1:
    xi = query[1]
    bag.append(xi)
  elif query[0] == 2:
  
    xi = query[1]
    bag = list(map(lambda x:x+xi,bag))
  else:
  
    bag.sort()
    ans.append(bag[0])
    bag.remove(bag[0])
# print(bag)
# print(ans)

for x in ans:
  print(x)


# -----------------------------------------------------

# 理解度C
# マルチセット　ヒープ
