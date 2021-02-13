h, w = map(int, input().split())
field = []
is_full = True
for i in range(h) :
  row = []
  data = input()
  for j in data :
    if j == "#" :
      row.append(1)
      continue
    is_full = False
    row.append(0)
  field.append(row)
  
def road_search(base, is_see_h, points) :
  next_bases = []
  i_set = set([])
  j_set = set([])
  if is_see_h :
    j_set.add(base)
    for i in range(1, h-1) :
      if field[i][base] == 1 and [i, base] not in points :
        next_bases.append(i)
        i_set.add(i)
  else :
    i_set.add(base)
    for j in range(1, w-1) :
      if field[base][j] == 1 and [base, j] not in points :
        next_bases.append(j)
        j_set.add(j)
  # print(next_bases)
  if len(next_bases) == 0 :
    return i_set, j_set
  else :
    if is_see_h :
      next_points = []
      for next_base in next_bases :
        next_points.append([next_base, base])
      for next_base in next_bases :
        next_i_set, next_j_set = road_search(next_base, False, next_points)
        i_set |= next_i_set
        j_set |= next_j_set
      return i_set, j_set
    else :
      next_points = []
      for next_base in next_bases :
        next_points.append([base, next_base])
      for next_base in next_bases :
        next_i_set, next_j_set = road_search(next_base, True, next_points)
        i_set |= next_i_set
        j_set |= next_j_set
      return i_set, j_set 

i_set = set([])
j_set = set([])
for i in range(h) :
  if field[i][0] == 1 or field[i][w-1] == 1 :
    i_set.add(i)
    for j in range(1, w-1) :
      # print(field[i][j] == 1)
      if field[i][j] == 1 :
        next_i_set, next_j_set = road_search(j, True, [i, j])
        i_set |= next_i_set
        j_set |= next_j_set
        
for j in range(w) :
  if field[0][j] == 1 or field[h-1][j] == 1 :
    j_set.add(j)
    for i in range(1, h-1) :
      if field[i][j] == 1 :
        next_i_set, next_j_set = road_search(i, False, [i, j])
        i_set |= next_i_set
        j_set |= next_j_set
        
c_i = h
c_j = w
# print(i_set)
# print(j_set)
if 0 in i_set :
  if h-1 in i_set :
    c_i -= len(i_set)
  else :
    c_i -= len(i_set) + 1
else :
  c_i -= len(i_set) + 2
if 0 in j_set :
  if w-1 in j_set :
    c_j -= len(j_set)
  else :
    c_j -= len(j_set) + 1
else :
  c_j -= len(j_set) + 2

if is_full :
  print(0)
elif c_i < 0 or c_j < 0 :
  print(0)
elif c_i < c_j :
  print(c_i)
else :
  print(c_j)