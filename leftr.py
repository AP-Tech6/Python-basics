#code for left rotation of an list by n elements
#l=list(map(int,input().split()))
#first=l[0]
#for i in range(len(l)-1):
    #l[i]=l[i+1]
#l[-1]=first
#print(l)

#code for left rotation for 2 places
l=list(map(int,input().split()))
first=l[0]
second=l[1]
for i in range(len(l)-2):
    l[i]=l[i+2]
l[-2]=first
l[-1]=second
print(l)
