def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
    if n != 1:
        print(n)

n = int(input())
count(n)