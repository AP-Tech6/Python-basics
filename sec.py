#code for second largest number in a list without using sorting
l=list(map(int,input().split()))
m1,m2=0,0
for i in l:
    if i>m1:
        m2=m1
        m1=i
    elif i>m2 and i!=m1:
        m2=i
print(m2)


trace output for input 1 2 3 4 5 6 7 
m1=0,m2=0
i=1, m1=1,m2=0
i=2, m1=2,m2=1
i=3, m1=3,m2=2
i=4, m1=4,m2=3
i=5, m1=5,m2=4
i=6, m1=6,m2=5
i=7, m1=7,m2=6
print(m2)
trace output for input 5 4 3 2 1
m1=0,m2=0
i=5, m1=5,m2=0
i=4, m1=5,m2=4
i=3, m1=5,m2=4
i=2, m1=5,m2=4
i=1, m1=5,m2=4
print(m2)












