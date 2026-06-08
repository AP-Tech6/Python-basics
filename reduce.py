def fun(n):
    if(n==0):
        return 
    elif(n==1):
        return 0
    elif(n%2==0):
        return 1+fun(n/2)
    else:
        return 1 + min(fun(n-1), fun(n+1))
n=int(input())
print(fun(n))    
