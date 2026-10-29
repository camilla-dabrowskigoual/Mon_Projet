L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
for i in L :
    if i%2 != 0 :
        L.remove(i)
print(L)
print(sum(L))