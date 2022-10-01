d = {}
for i in range(1, 101):
    d[i] = 0
print(d)
for i in range(1, 101):
    for j in range(1, 101):
        if j % i == 0:
            if d[j] == 0:
                d[j] = 1
            else:
                d[j] = 0
c = 0
print(d)
for i in d:
    if d[i] == 1:
        c = c+1
print(c)
