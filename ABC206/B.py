N = int(input())

# i日目のお金はいくらか？
# (d+1)*d//2
def total(d):
  return (d+1)*d//2

d = 1
while(total(d) < N):
  d+=1
print(d)