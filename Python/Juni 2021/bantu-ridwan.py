a = [4,2,3,3,5,1,5,4]

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(a[i])
