# o -> 含まれてる
# x -> 含まれてない
# ? -> わからない

# 考察
# 全パターン調べても 4桁なので 10000回で済む
# 0から始まる場合もあるので1000から始めるのは無理
# ? は入っていても入っていなくても良いので考えない
s = input()
count = 0

for i in range(10000):
  isOK = True
  # 4桁の形に変形する
  x = str(i).zfill(4)

  for j in range(10):
    # 必要なものが含まれてなければX
    if s[j] == "o" and str(j) not in x:
        isOK = False
    # 不必要なものが含まれていてもX
    if s[j] == "x" and str(j) in x:
      isOK = False


  if isOK:
    count += 1  
  


print(count)
