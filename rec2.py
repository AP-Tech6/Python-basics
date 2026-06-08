def count(n):
    if n == 0:
        return
    else:
        count(n-1)
        print(n)

n = int(input())
count(n)