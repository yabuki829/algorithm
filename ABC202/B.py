# https://atcoder.jp/contests/abc202/tasks/abc202_b

# 0 を 0 に、
# 1 を 1 に、
# 6 を 9 に、
# 8 を 8 に、
# 9 を 6 に変換する
s = input()

# 反転する
s = s[::-1]
ans = ""
for i in range(len(s)):
  if s[i] == "0" :
    ans+="0"
  elif s[i] == "1":
    ans += "1"
  elif s[i] == "6":
    ans += "9"
  elif s[i] == "8":
    ans += "8"
  elif s[i] == "9":
    ans += "6"

print(ans)
    