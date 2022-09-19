i = int(input("enter a number "))

count = 0
for i in str(i):
    if i == "3":
        count = count+1

if count == 1:
    lol = 0
    for j in range(2, int(i)//2):
        if i % j == 0:
            lol = lol+1
    if lol == 0:
        print(True)
    else:
        print(False)

else:
    print(False)
