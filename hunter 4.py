in=int(input()) 
mo=list(map(int,input().split()[:in]))
for i in mo:
  if mo.count(i)==2:
    pass
  else:
    print(i)
