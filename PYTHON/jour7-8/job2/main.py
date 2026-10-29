x = "_"
y = "/"
z = "\\"
n=5

def triangle(n) :
    print(" "*(n-1)+y+z+" "*(n-1))
    for i in range (2, n):
        print(" "*(n-i)+y+" "*(i*2-2)+z)
    print(y+x*(2*n-2    )+z)
triangle(n)