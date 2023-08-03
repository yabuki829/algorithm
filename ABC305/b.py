p,q = map(str,input().split())



dis = [0,3,1,4,1,5,9]
# 累積和
ruisekiwa = [0] * 7
for i in range(7):
  ruisekiwa[i] = dis[i] + ruisekiwa[i-1]



if p < q:
  p,q = q,p
print(ruisekiwa[ord(p)-65] - ruisekiwa[ord(q)-65])
  