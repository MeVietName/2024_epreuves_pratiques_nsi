def moyenne(notes) -> float:
    length = len(notes)
    for i in range(length):
        valeur = valeur + notes[i][0] * notes[i][1]
    return valeur // length
    
    
# 9.142857142857142
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))

# None
print(moyenne([(3, 0), (5, 0)]))