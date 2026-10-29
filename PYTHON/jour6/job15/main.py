L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

#on arrondit :
Lbis = []
for i in L :
    if i not in Lbis :
        i = i//1
        Lbis.append(i)
print(Lbis)

#on range dans l'ordre croissant sans utiliser sort() :
for i in range(0,9):
    for j in range(i+1, 9):
        if Lbis[i]>Lbis[j]:
            Lbis[i], Lbis[j]=Lbis[j], Lbis[i]
print(Lbis)
        