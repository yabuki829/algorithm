T=int(input())


def resolve():
 
  n,d,k = map(int,input().split())
  isOK = [False] * n
  
  isOK[0] = True 
  ans = [0]

  for i in range(n-1):
    x = (ans[-1] + d) % n
    # isOkのx番目がTrueであれば 
   
    if x < n: 
      if isOK[x] == False:
        isOK[x] = True
        
        ans.append(x)
      else: 
        for j in range(1,n+1):
          x = (ans[-1]+j + d) % n
          if x < n: 
            if isOK[x] == False:
              isOK[x] = True
              ans.append(x)
              break
          
  print(ans[k-1])
    # ans[-1] + 1 でもう一度




for _ in range(T):
  resolve()

