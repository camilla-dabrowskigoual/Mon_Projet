#déterminer si les 3 longueurs peuvent former un triangle

a = int(input("longueur a ="))
b = int(input("longueur b ="))
c = int(input("longueur c ="))
print("la longueur maximale est : ", max(a,b,c))

if max(a,b,c)< ((a+b+c)-max(a,b,c)):
    print("les 3 longueurs permettent de former un triangle")
else :
    print("les 3 longueurs ne permettent pas de former un triangle")
    exit()
    

#savoir si le triangle est isocèle, équilatèrale ou quelconque 

if(a != b and a != c and b != c):
    print("le triangle est quelconque")
elif(a == b and b == c and a == c):
    print("le triangle est equilateral")
elif(a == c or a == b or b == c):
    print("le triangle est isocèle")

#savoir si le triangle est rectangle
midle = (a+b+c)-max(a,b,c)-min(a,b,c)
if max(a,b,c)**2 == min(a,b,c)**2 + midle**2 :
    print("le triangle est rectangle")
else :
    print("le triangle n'est pas rectangle")