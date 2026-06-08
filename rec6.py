def count(n):
    if n <= 0:
        return
    else:
        print(n)
        count(n-2)
        if(n!=2):
            print(n)
n = int(input())

count(n)