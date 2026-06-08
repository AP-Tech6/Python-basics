def count(n):
    if n ==0:
        return 200
    else:
        t=count(n-1)
        print(n)
        return t
      
n = int(input())
print(count(n))
