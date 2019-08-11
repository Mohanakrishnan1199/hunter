m=int(input())
mo=list(map(int,input().split()[:m]))
d=[]
for i in mo:
    if mo.count(i)>1:
        h=i
        for j in range(0,len(mo)):
            if mo[j]==h:
                if j%2==0:
                    if h%2!=0:
                        if h not in d:
                            d.append(h)
                        
            else:
                if h%2==0:
                    if h not in d:
                        d.append(h)
    else:
        k=mo.index(i)
        if k%2==0:
            if i%2!=0:
                if h not in d:
                    d.append(h)
        else:
            if i%2==0:
                if h not in d:
                    d.append(h)
print(*d)
