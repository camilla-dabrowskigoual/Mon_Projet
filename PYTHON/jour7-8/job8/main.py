liste = [3, 12, 16, 7, 8, 1, 0, 15]

def my_sort(liste):
    z =0
    for j in range(len(liste)) : #on répete l'opération autant de fois qu'il y a d'élements dans la liste 
        for i in range(len(liste)-1): #on compare chaque élement de la liste avec l'élement adjacent
            if liste[i]>liste[i+1]:
                  liste[i], liste[i+1] = liste[i+1], liste[i]
                  z=z+1
    print("Liste triée :", liste)
    print("Nombre total de coups pour trier la liste :",z)

my_sort(liste)



a = 5
def fin (x):
    a == a+x
    return a
print(fin(3))
    