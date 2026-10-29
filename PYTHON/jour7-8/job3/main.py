n = 10  
x = "#"
y = "|"

def tapis(n):
    print(1," " +"+"+(n+1)*"-" + "+")
    for i in range(2, n+3):
        if i>= 10 :
            print(i,y+(n+2-i)*x+" "+ x*(i-2)+y)
        elif i<10 :
            print(i," "+ y+(n+2-i)*x+ " "+ x*(i-2)+y)
    print(n+3, "+" + (n+1)*"-" + "+")

tapis(n)