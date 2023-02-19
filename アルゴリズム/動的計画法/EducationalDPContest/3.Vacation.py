# 夏休み　幸福度
# https://atcoder.jp/contests/dp/tasks/dp_c

# 3
# 10 40 70
# 20 50 80
# 30 60 90


n = int(input())

happy = []
for i in range(n):
  a,b,c = map(int,input().split()) 
  
  happy.append([a,b,c])
dp = [[0]*3 for _ in range(n)]
# dp[i][x]  = i日目にxに行くときのi日目までの幸福の総和の最大値を表す
#
# x = 0->海
#     1->むし
#     2->宿題


dp[0] = happy[0]

# print("DP",dp)
# 0,1~n日め
for i in range(1,n):
  for now_place in range(3):
    for last_place in range(3):
      # 昨日行った場所は行くことができない
      if now_place != last_place:
        
        a = dp[i][now_place]
        b = dp[i-1][last_place] + happy[i][now_place]
        dp[i][now_place] = max(a,b)


ans = 0
for i in range(3):
  ans = max(ans,dp[-1][i])
print(ans)

