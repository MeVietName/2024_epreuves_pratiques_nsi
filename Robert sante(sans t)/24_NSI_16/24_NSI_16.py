def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(len(tab)): 
        for j in range(i, len(tab)): 
            if tab[i] > tab[j]: 
                echange(tab, j, i) 
    return tab

# []
print(tri_bulles([]))

# [1, 2, 3, 3, 6, 7, 9]
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))

# [3, 4, 7, 9]
print(tri_bulles([9, 7, 4, 3]))