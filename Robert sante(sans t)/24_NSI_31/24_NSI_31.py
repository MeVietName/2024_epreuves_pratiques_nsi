def dichotomie(tab: list, x: int):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut + ((fin - debut) // 2) #bien se rappeller 
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

# True
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))

# False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))



