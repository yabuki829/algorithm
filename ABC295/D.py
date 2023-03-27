s = input()

from itertools import product
import collections

s_list = [int(i) for i in s]

s_set_list = list(set(s_list))
ans = 0
for bits in product([0, 1], repeat=len(s)):
  a_select = []
  for i in range(len(bits)):
    if  bits[i] == 1:
     a_select.append(s_list[i])

  s_counter = collections.Counter(a_select)
  if len(a_select) % 2  == 0:
    for i in s_set_list:
      if s_counter[i] % 2 != 0:
        continue
  
    ans+= 1
print(ans)

