a=input()
d={}
for i in a:
  d[i]=0
for i in a:
  d[i]+=1
for i in a:
  if(d[i]==1):
    print(i,end="")
