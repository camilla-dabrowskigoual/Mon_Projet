def repas(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte,topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaud, aubergine, navet")
repas("fruits", "été")
repas("légume", "hiver")
repas("fruits", "hiver")
repas("légume","hiver")
repas(type="fruits", saison="hiver")