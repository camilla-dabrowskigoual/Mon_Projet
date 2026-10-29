for i in range(2, 1001):
    z = 0
    for j in range(1, i+1):
        if i%j == 0 :
            z=z+1
    if z == 2 :
        print(i)