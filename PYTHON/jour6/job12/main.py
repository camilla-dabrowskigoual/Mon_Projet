L = [34,15,7,12,39,67,15]
for i in range(0, 7):
    for j in range(i+1, 7):
        if L[i]>L[j]:
            L[i], L[j]=L[j], L[i]
print(L)