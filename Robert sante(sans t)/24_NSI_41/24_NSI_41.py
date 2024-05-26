def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins

# [7, 4, 8, 9]
print(ajoute(1, 4, [7, 8, 9]))

# [7, 8, 9, 4]
print(ajoute(3, 4, [7, 8, 9]))

# [4, 7, 8, 9]
print(ajoute(0, 4, [7, 8, 9]))
