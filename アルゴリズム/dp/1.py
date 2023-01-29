
# ------------------------------------------------

# 一番簡単な例題
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
# 問題　コイン
#　額面がC1,C2,..., Cm　円の M種類のコインを使って、 N 円を支払うときの、コインの最小の枚数を求めて下さい。
# 各額面のコインは何度でも使用することができます。

# 6 15
# 1 2 7 8 12 50


# 今回の問題は,1,2,7,8,12,50を使って「15」を作る。
M=6
N=15
conins = [1,2,7,8,12,50]

opt = [float("inf")]*(N+1)
# opt[0] = 0
# opt[1] = 1
# opt[2] = 1
# opt[3] = 2 [1,2]
# opt[4] = 2 [2,2]
# opt[5] = 3 [1,2,2]

opt[0] = 0
# aは1~Nまで

for a in range(1,N+1):
  for c in conins:
    if a >= c:
      opt[a] = min(opt[a-c]+1,opt[a]) 

if opt[N] == float("inf"):
  print("作成できませんでした")
else:
  print(opt[N])


