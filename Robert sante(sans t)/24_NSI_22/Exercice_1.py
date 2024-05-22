def recherche_indices_classement(elt: int, tab: list)-> list:
    length = len(tab)
    inferieur = []
    egal = []
    superieur = []
    for i in range(length):
        if tab[i] < elt:
            inferieur.append(i)
        if tab[i] == elt: 
            egal.append(i)
        if tab[i] > elt:
            superieur.append(i)
    return inferieur, egal, superieur


# ([0, 3, 7], [1, 6], [2, 4, 5])
print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))

# ([0, 2, 5], [], [1, 3, 4])
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))

# ([0, 1, 2, 3], [], [])
print(recherche_indices_classement(3, [1, 1, 1, 1]))

# ([], [], [])
print(recherche_indices_classement(3, []))
