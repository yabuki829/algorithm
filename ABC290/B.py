# 10 3
# oxxoxooxox

n,k = map(int,input().split())
s = input()

ans = ""
ok = 0
for i in range(n):
  if ok < k:
    if s[i] == "o":
      ok+=1
      ans+="o"
    else:
      ans+="x"
  else:
    ans+="x"
    
print(ans)
# oxxoxoxxxx
# oxxoxoxxxx
