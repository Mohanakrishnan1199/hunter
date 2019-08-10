m=int(input())
m2=list(map(int,input().split()))
m3=[]
for i in m2:
  if i in m3:
    print(i)
    break
  m3.append(i)  
else:
  print("unique")
