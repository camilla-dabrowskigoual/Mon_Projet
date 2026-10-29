nombre = int(input("entrez un nombre positif :"))
def valeur (nombre):
    if nombre <= 0 :
        print("recommencez avec un nombre positif")
        exit()
    else :
        if nombre%2 == 0 :
            print("le nombre est pair")
        else :
            print("le nombre est impair")
valeur(nombre)