b, c = map(int, input().split())
if c == 1 :
  if b == 0 :
    print(1)
  else :
    print(2)
else :
  if b == 0 :
    print(c)
  elif b > 0 :
    if 2*b <= c :
      print(c+2*b-1)
    else :
      print(2*c-1)
  else :
    if 2*(-1*b) < c :
      print(c+2*(-1*b))
    else :
      print(2*c-1)