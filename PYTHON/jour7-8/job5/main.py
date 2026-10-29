def distance(x,y):
    # pour 1 aller aux WC :
    d1 = (x*y)*10**-2
    print("Pour 1 aller aux WC, le gardien parcourt", d1, "mètres")
    # pour 1 aller/retour :
    d2 = 2 * d1
    print("Pour 1 aller/retour aux WC, le gardien parcourt", d2, "mètres")
    # par jour, le gardien va 5x aux WC donc :
    d3 = 5 * d2
    print("Par jour, le gardien parcourt", d3, "mètres")
    # pour 1 semaine de 7 jours :
    z = 7 * d3
    print(f"Pour {x} marches de {y} cm, le gardien parcourt {z} m par semaine")
distance(150, 20)
distance(20,5)

