n=int(input()) 
m=list(map(int,input().split()[:n]))
for i in m:
  if m.count(i)==2:
    pass
  else:
    print(i)
