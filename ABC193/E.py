t = int(input())
for i in range(t) :
  x, y, p, q = map(int, input().split())
  first_b_start = x
  first_b_end = x + y
  train_cycle_start = 2*x + y
  train_cycle_end = 2*x + 2*y
  awake_cycle_start = p
  awake_cycle_end = p + q
  now = 0
  if first_b_start <= awake_cycle_start or awake_cycle_end < first_b_end :
    print(p)
  else :
    for j in range(1000) :
      for k in range(1000) :
      	if train_cycle_start*j + x <= awake_cycle_start*k or \
        train_cycle_end*j + x < awake_cycle_end*k :
          print(awake_cycle_start*k)
          break
      else :
        break