l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    first=l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    l[-1]=first
print(l)