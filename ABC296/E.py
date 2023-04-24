# https://atcoder.jp/contests/abc296/tasks/abc296_e
# 3
# 2 2 3


# 1. 青木さんがKiを指定する
# 2. 高橋さんが1〜N以下のSiを選び黒板に書く
# 3. Ki 回 
#       黒板に書かれているものがxであればA[x] を黒板に書く
# 4. Ki回捜査終了後
#     黒板の文字がiならi回目のゲームは高橋さんの勝ち

N = int(input())
A = list(map(int,input().split()))


# 水色dif
# これグラフ問題らしいけどこれはでてこん
# 今はまだむり