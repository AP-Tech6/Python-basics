def count(n,m=0):
    if n == m:
        return
    print(m+1) 
    count(n,m+1)
    if(m+1!=n):
        print(m+1)
    
n = int(input())
count(n)