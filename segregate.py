l=list(map(int,input().split()))
l.sort()
result=[]
for i in l:
    if i%2!=0:
        result.append(i)
    else:
        result.insert(0,i)
print(result)

#sample input:
#1 2 3 4 5 6 7 8 9
#sample output:
#[8, 6, 4, 2, 1, 3, 5, 7, 9]