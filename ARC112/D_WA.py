h, w = map(int, input().split())
field = []
is_full = True
is_null = True
for i in range(h) :
  row = []
  data = input()
  for j in data :
    if j == "#" :
      row.append(1)
      is_null = False
      continue
    is_full = False
    row.append(0)
  field.append(row)
  
def check_is_enough(a_set, a_list):
  is_enough = True
  for n in a_list :
    if not n in a_set :
      is_enough = False
  return is_enough
  
def road_search(base, is_see_h, points):
  next_bases = []
  i_set = set([])
  j_set = set([])
  if is_see_h :
    j_set.add(base)
    for i in range(1, h-1) :
      if field[i][base] == 1 and [i, base] not in points :
        next_bases.append(i)
        i_set.add(i)
        if check_is_enough(i_set, range(1, h-1)) and h<=w :
          return i_set, j_set
  else :
    i_set.add(base)
    for j in range(1, w-1) :
      if field[base][j] == 1 and [base, j] not in points :
        next_bases.append(j)
        j_set.add(j)
        if check_is_enough(j_set, range(1, w-1)) and w<=h:
          return i_set, j_set
  # print(next_bases)
  if len(next_bases) == 0 :
    return i_set, j_set
  else :
    if is_see_h :
      next_points = points
      for next_base in next_bases :
        next_points.append([next_base, base])
      for next_base in next_bases :
        next_i_set, next_j_set = road_search(next_base, False, next_points)
        i_set |= next_i_set
        j_set |= next_j_set
      return i_set, j_set
    else :
      next_points = points
      for next_base in next_bases :
        next_points.append([base, next_base])
      for next_base in next_bases :
        next_i_set, next_j_set = road_search(next_base, True, next_points)
        i_set |= next_i_set
        j_set |= next_j_set
      return i_set, j_set 

if not(is_full or is_null) :
  i_set = set([])
  j_set = set([])
  for i in range(h) :
    if field[i][0] == 1 or field[i][w-1] == 1 :
      i_set.add(i)
      if field[i][0] == 1 :
        j_set.add(0)
      else :
        j_set.add(w-1)
      for j in range(1, w-1) :
        # print(field[i][j] == 1)
        if field[i][j] == 1 :
          next_i_set, next_j_set = road_search(j, True, [i, j])
          i_set |= next_i_set
          j_set |= next_j_set
        if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
        (check_is_enough(i_set, range(1, h-1)) and h<=w) :
          break
      else :
        break
    if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
    (check_is_enough(i_set, range(1, h-1)) and h<=w) :
      break

  for j in range(w) :
    if field[0][j] == 1 or field[h-1][j] == 1 :
      j_set.add(j)
      if field[0][j] == 1 :
        i_set.add(0)
      else :
        i_set.add(h-1)
      for i in range(1, h-1) :
        if field[i][j] == 1 :
          next_i_set, next_j_set = road_search(i, False, [i, j])
          i_set |= next_i_set
          j_set |= next_j_set
        if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
        (check_is_enough(i_set, range(1, h-1)) and h<=w) :
          break
      else :
        break
    if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
    (check_is_enough(i_set, range(1, h-1)) and h<=w) :
      break
      
  c_i = h
  c_j = w
  # print(sorted(list(i_set)))
  # print(sorted(list(j_set)))
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
  # print(c_i, c_j)
  
  news = []
  row = [True]
  for i in range(1, h-1) :
    if field[i][0] != 1 and i not in i_set :
      row.append([i, 0])
  news.append(row)
  row = [False]
  for j in range(1, w-1) :
    if field[0][j] != 1 and j not in j_set:
      row.append([0, j])
  news.append(row)
  # print(news)
  i_completes = 0
  j_completes = 0
  for row in news :
    for p, q in row[1:] :
      if row[0] == True :
        for j in range(1, w-1) :
          # print(field[i][j] == 1)
          if field[p][j] == 1 and p not in i_set :
            next_i_set, next_j_set = road_search(j, True, [p, j])
            i_set |= next_i_set
            j_set |= next_j_set
            # print(next_i_set, next_j_set)
            i_completes += len(next_i_set) - 1
            j_completes += len(next_j_set) - 1
          if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
          (check_is_enough(i_set, range(1, h-1)) and h<=w) :
            break
        else :
          break
      else :
        for i in range(1, h-1) :
          if field[i][q] == 1 and q not in j_set :
            next_i_set, next_j_set = road_search(i, False, [i, q])
            i_set |= next_i_set
            j_set |= next_j_set
            # print(next_i_set, next_j_set)
            i_completes += len(next_i_set) - 1
            j_completes += len(next_j_set) - 1
          if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
          (check_is_enough(i_set, range(1, h-1)) and h<=w) :
            break
        else :
          break
      if (check_is_enough(j_set, range(1, w-1)) and w<=h) or \
      (check_is_enough(i_set, range(1, h-1)) and h<=w) :
        break
    else :
      break

if is_full :
  print(0)
elif is_null :
  if h < w :
    print(h-2)
  else :
    print(w-2)
elif c_i - i_completes < 0 or c_j - j_completes < 0 :
  print(0)
elif c_i - i_completes < c_j - j_completes :
  print(c_i - i_completes)
else :
  print(c_j - j_completes)