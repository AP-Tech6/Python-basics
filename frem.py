#now for maximum frequency
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
elemnt=0
for i in d:
    if d[i]>m:
        m=d[i]
        elemnt=i
print(elemnt) 