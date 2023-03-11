# https://atcoder.jp/contests/abc292/tasks/abc292_c
N=int(input())

# まずはA*Bの計算結果を作る -> cnt
cnt = [0] * (N+1)
for a in range(1,N):
  for b in range(1,N):
    if a*b<=N:
      cnt[a*b] += 1
    else:
      break


ans = 0
for i in range(1,N):
  # ABがiになる組み合わせの個数 
  # CDがN-1になる組み合わせの個数
  # 例) N=4, i=1の場合
  #     ans+= cnt[1] * cnt[3]  # cnt[1] = ABが1になる組み合わせの個数 
  ans += cnt[i]*cnt[N-i] 
print(ans)

# 計算結果を使う