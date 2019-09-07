a=int(input())
l=list(map(str,input().split()[:a]))
b=l.count('P')
c=(b/a)*100
if int(c)<25:
   print("Blacklisted")
else:
   print("Not Blacklisted")
