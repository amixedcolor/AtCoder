import itertools

b, c = map(int, input().split())
choices_list = [[True,False] for i in range(c)]
a = 1
i_set = set((b,))
for choices in itertools.product(*choices_list):
  i = b
  j = c
  loop = 0
  for choice in choices :
    loop += 1
    if choice :
      i *= -1
      j -= 1
    else :
      i -= 1
      j -= 2
    if j >= 0 :
      if i not in i_set :
        # print(i, j, choices[:loop])
        a += 1
        i_set.add(i)
      if j == 0 :
        break
    else :
      i += 1
      if i not in i_set :
        # print(i, j, choices[:loop])
        a += 1
        i_set.add(i)
      break
print(a)