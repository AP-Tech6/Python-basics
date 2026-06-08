def count(n):
    if n <= 0:
        return
    else:
        print(n)
        count(n-2)
n = int(input())

count(n)