l=list(map(int,input().split()))
res=[]
for i in L:
    if i not in res and l.count(i) % 2 != 0:
        res.append(i)
print(res)

#question: Given a list of integers, write a program to find all the integers that occur an odd number of times in the list and
# return them in a new list. 
#The order of the integers in the output list should be the same as their first occurrence in the input list.