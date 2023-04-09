H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)
# 操作
# S[i][j]番目が"T" ,S[i][j+1]もT ものを選ぶ
# S[i][j]をPに置き換え, S[i][j+1]をCに置き換える

def result(s):
  for i in range(W-1):
    if s[i] == s[i+1] and s[i] == "T":
      s[i] = 'P'
      s[i+1] = 'C'
  return s

for i in range(H):
    s = list(S[i])
    s = result(s) 
    print(''.join(s)) 