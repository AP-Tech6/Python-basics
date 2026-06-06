#right rotation of list of 1 place
l=list(map(int,input().split()))
last=l[-1]
for i in range(len[l]-1,0,-1):
    l[i]=l[i-1]
l[0]=last
print(l)  
