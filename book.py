l = list(map(int, input().split()))
k = 3
m = 0
for i in range(len(l) - k + 1):
    s = 0
    for j in range(i, i + k):
        s = s + l[j]
    m = max(m, s)
print(m)