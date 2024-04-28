def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(0, N): 
        imin = k
        for i in range(imin, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, i, k) 

tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
print(tab)
