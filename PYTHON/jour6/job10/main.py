L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
L.sort()
print(L)
Lbis = L[6:-2]
print(Lbis)

#méthode 1
produit = Lbis[0]*Lbis[1]*Lbis[2]
print(produit)

#méthode 2
i = 0
z = 1
for i in Lbis :
    z = z*i
print(z)