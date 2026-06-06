l = list(map(int, input().split()))
result = []
for i in l:
    if i not in result:
        result.append(i)

print(result)

# Sample Input:
# 1 1 2 3 1 2
# Sample Output:
# [1, 2, 3]
