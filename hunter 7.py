m=int(input())
mo=list(map(int,input().split()))[:m]
k=[]
for i in range(0,m):
  if(mo[i]%2==0 and i%2==1 or mo[i]%2==1 and i%2==0):
    k.append(mo[i])
print(*k,end="")
