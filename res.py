# given 2 sorted lists, merge them into one sorted list

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

result = []

i = 0
j = 0

while(i < len(l1) and j < len(l2)):

    if l1[i] < l2[j]:
        result.append(l1[i])
        i = i + 1

    else:
        result.append(l2[j])
        j = j + 1

while(j < len(l2)):
    result.append(l2[j])
    j = j + 1

while(i < len(l1)):
    result.append(l1[i])
    i = i + 1

print(result)