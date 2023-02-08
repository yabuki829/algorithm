# 問題　https://atcoder.jp/contests/abc155/tasks/abc155_d

n,k = int(input.split())

A = list(map(int, input().split()))

# 二分探索を使う

# テクニック
# 全通りのK番目を答えよと言われたら真っ先に二分探索を疑う