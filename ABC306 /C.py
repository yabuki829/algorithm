n = int(input())
A = list(map(int,input().split()))

# dp[i][poz] i個目まで食べ物が出てきて、pozは今、毒状態かどうか　= 食べた料理の美味しさの総和
# 二次元DP
