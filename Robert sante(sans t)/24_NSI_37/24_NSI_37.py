def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab) - 1 # dernier indice de la zone non triée //// bien pensera mettre la (longueur - 1)
    while i < j:
        if tab[i] == 0:
            i = i + 1 
        else:
            valeur = tab[j] 
            tab[j] = 1  #bien penser a mettre 1
            tab[i] = valeur
            j = j - 1
    return tab

# [0, 0, 0, 0, 0, 1, 1, 1, 1]
print(tri([0,1,0,1,0,1,0,1,0]))


