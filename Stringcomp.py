s = input()
prev = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == prev:
        count = count + 1
    else:
        print(f"{prev}{count}", end="")
        prev = s[i]
        count = 1
print(f"{prev}{count}")