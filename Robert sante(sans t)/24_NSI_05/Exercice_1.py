def max_et_indice(tab):
    comparateur = tab[0]
    # ["valeur", "index"]
    idk = [tab[0], 0]
    
    for i in range(len(tab)):
        if comparateur < tab[i]:
            comparateur = tab[i]
            idk[0] = tab[i]
            idk[1] = i
    return idk


# version un peu ameliorer juste le return et index qui est different, return directement les deux valeurs separe au lieu de faire une liste
def max_et_indicev2(tab):
    valeurmax = tab[0]
    indexmax = 0
    for i in range(len(tab)):
        if valeurmax < tab[i]:
            valeurmax = tab[i]
            indexmax = i
    return (valeurmax, indexmax)
        


# 9, 3
print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indicev2([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))


# -2, 0 
# print(max_et_indice([-2]))
# print(max_et_indicev2([-2]))

# 3, 2
# print(max_et_indice([-1, -1, 3, 3, 3]))
# print(max_et_indicev2([-1, -1, 3, 3, 3]))