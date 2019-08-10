n=int(input()) 
m=list(map(int,input().split()[:n]))
k=[]
count=0
for i in m:
  if i==count:
    k.append(i)
  count+=1
if len(k)>1:
  print(*sorted(k))
else:
  print(-1)
