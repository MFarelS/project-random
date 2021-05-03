k = 1
for i in range(1,6):
    for j in range(1,i):
        print(k,end=" ")
        if k == 1 or k == 6:
            k = k + 3
        elif k == 13:
            k = k + 4
        else:
            k = k + 2
    print("")
