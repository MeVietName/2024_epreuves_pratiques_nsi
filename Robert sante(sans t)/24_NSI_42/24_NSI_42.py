def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2  # bien mettre (debut + fin // 2) 
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

# True
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))

# False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))

# False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))

# False
print(dichotomie([], 28))