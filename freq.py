l=list(map(int,input().split()))
c=0
m=0
for i in l:
    m=max(m,i)
for i in l:
    if i==m:
        c=c+1
print(c)        