def digitize(n):
    l = str(n)
    new = []
    for i in l:
        new.append(int(i))
    return list(reversed(new))

print(digitize(12345))