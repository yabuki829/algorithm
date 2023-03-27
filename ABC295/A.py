n = input()

list = list(map(input().split()))

for s in list:
  # and, not, that, the, you 
  if s == "and" or s == "not" or s == "that" or s == "the" or s == "you":
    print("Yes")
    exit()

print("No")
  