notes = [43, 23, 32, 52, 61, 45, 67, 89, 87, 76, 12, 80]

def notes_finales(notes):
    notes_arrondies = []
    liste=[]

    for i in notes :
        if i<= 40 :
            notes_arrondies.append(i)
        elif i> 40 :
            while i%5 != 0 :
                i = i+1
            notes_arrondies.append(i)


    for j in range(len(notes)):
        if notes_arrondies[j]-notes[j]<3 :
            liste.append(notes_arrondies[j])
        elif notes_arrondies[j]-notes[j]>= 3 :
            liste.append(notes[j])
    print(liste)

notes_finales(notes)





