note1 = float(input("note1="))
note2 = float(input("note2="))
note3 = float(input("note3="))

def moyenne(note1, note2, note3):
    return((note1+note2+note3)/3)
moyenne_etudiant = moyenne(note1, note2, note3)
print("la moyenne de l'étudiant est de :", moyenne_etudiant, "/20")

if   15 <= moyenne_etudiant <= 20 :
    print("Très bon élève")
elif 10 <= moyenne_etudiant < 15 :
    print("Bon élève")
elif 7<= moyenne_etudiant < 10:
    print("Elève moyen")
elif 0 <= moyenne_etudiant < 7:
    print("Eleve devant faire des efforts")
    






