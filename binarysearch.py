l = sorted(list(map(int, input().split())))
print(l)
key = int(input())
low = 0
high = len(l) - 1

flag = 0
while low <= high:
    mid = (low + high) // 2
    if l[mid] == key:
        pos=mid
        flag = 1
        break
    elif l[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if flag == 1:
    print("key found at position", pos)
else:
    print("key not found")