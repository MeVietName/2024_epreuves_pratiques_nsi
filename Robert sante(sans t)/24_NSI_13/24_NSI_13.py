def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i + 1 
    return tab_a


# [1, 2, 3, 4, 5]
print(insere([1, 2, 4, 5], 3))

# [1, 2, 7, 12, 14, 25, 30]
print(insere([1, 2, 7, 12, 14, 25], 30))