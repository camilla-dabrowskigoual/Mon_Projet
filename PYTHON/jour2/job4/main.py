N = int(input("table de multiplication de:"))
for i in range(1, N+1) :
    print("table de multiplication de",i)
    for j in range(1,11):
        print(i, "x", j, "=", i*j)
