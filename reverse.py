l=list(map(int,input().split()))
n=len(l)//2
for i in range(n//2):
    temp=l[i]
    l[i]=l[n-i-1]
    l[n-i-1]=temp
print(l)

#left->anticlockwise
#right->clockwise