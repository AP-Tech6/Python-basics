l=list(map(int,input().split()))
k=int(input())
if l:
    k%=len(l)
    l=l[k:]+l[:k]
print(l)   