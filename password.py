s = input()

i = 0

if len(s) < 8:
    print("invalid")

elif " " in s:
    print("invalid")

else:

    for c in s:
        if c.isupper():
            i = i + 1
            break

    for c in s:
        if c.islower():
            i = i + 1
            break

    for c in s:
        if c.isdigit():
            i = i + 1
            break

    for c in s:
        if not c.isalnum():
            i = i + 1
            break

    if i == 4:
        print("valid")

    else:
        print("invalid")