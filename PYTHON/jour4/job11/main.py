nombre_entier = int(input("saisir un nombre entier (en minutes):"))
def time_to_text(nombre_entier):
    x = int(nombre_entier/60)
    y = nombre_entier - (x*60)
    print(nombre_entier, "fait",x,"heures et",y,"minutes")
time_to_text(nombre_entier)
                          