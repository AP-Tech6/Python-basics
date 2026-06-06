event=list(map(int,input().split()))
policec=0
unsolc=0
n=int(input("enter input: "))
for i in event:
    if i==1:
        policec+=i
    elif i==-1:
        if policec>0:
            policec-=1
        else:
            unsolc+=1
print(unsolc)

#sample input:
#1 1 -1 -1 1 -1
#sample output:
#0