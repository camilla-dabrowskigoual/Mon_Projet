a = 3
chaine = [["L", "-", "a", "-"], ["p", "-", "e", "-", "u","-", "r", "-"], ["e", "-" ,"s", "-", "t", "-"], ["l", "-", "e", "-"], ["c", "-" , "h", "-", "e", "-", "m", "-", "i", "-", "n", "-"], ["v", "-", "e", "-", "r", "-", "s", "-"], ["l", "-", "e", "-"], ["c", "-", "ô", "-", "t", "-", "é", "-"], ["o", "-",  "b", "-", "s", "-", "c", "-", "u", "-", "r", "-"]]
chaine_bis = []

def my_long_word(a, chaine):

    for i in chaine :
        z = 0
        for j in i :
            if j != "-" :
                z = z+1
        if z > a :
            chaine_bis.append(i)


    r = ""
    for i in chaine_bis :
        for j in i :
            if j != "-" :
                r = r + j
        r = r + " "
    return(r)

print(my_long_word(3, chaine))