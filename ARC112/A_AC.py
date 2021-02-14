t = int(input())
datas = []
for i in range(t) :
  l, r = map(int, input().split())
  datas.append([l, r])

for l, r in datas :
  if l == 0 and r == 0 :
    print(1)
  elif l == r :
    print(0)
  elif l*2 > r :
    print(0)
  else :
    print((r-l*2+1)*(1+r-l*2+1)//2)