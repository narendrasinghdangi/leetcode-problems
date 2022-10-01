c = 1
p = 1/5
r = 5
1
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if (i*c+j*p+k*r) == 100 and i+j+k == 100:
                print(i, j, k)
                break
