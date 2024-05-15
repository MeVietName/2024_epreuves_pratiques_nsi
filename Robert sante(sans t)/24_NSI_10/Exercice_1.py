def moyenne(notes) -> float:
    length = len(notes)
    valeur = 0
    nb_de_notes = 0
    for i in range(length):
        if notes[i][1] != 0:
            valeur = valeur + notes[i][0] * notes[i][1]
            nb_de_notes = nb_de_notes + notes[i][1]
    if nb_de_notes !=0:   
        return valeur / nb_de_notes
    else:
        return None
    
    
# 9.142857142857142
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))

# None
print(moyenne([(3, 0), (5, 0)]))