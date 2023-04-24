# 6
# MFMFMF

n = int(input())
s = input()

isM = False
if n > 1:
  if s[0] == "M":
    isM = True
else:
  print("Yes")
  exit()
  
for i in range(n-1):
  # １文字目がMの場合
  if s[i] == s[i+1]:
    print("No")
    exit()

   

print("Yes")



# 改善コード

# for i in range(n-1):
#   if s[i] == s[i+1]:
#     print("No")
#     exit()

# print("Yes")