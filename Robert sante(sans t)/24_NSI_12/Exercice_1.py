def tri_selection(tab):
    taille = len(tab)
    for i in range(taille-1):
        minimum = i 
        for k in range(i+1, taille): #taille ou taille-1 ?
            if tab[k] < tab[minimum]:
                minimum = k 
        if minimum != i:
            tab[i], tab[minimum] = tab[minimum], tab[i]
    return tab
            

# [-9, 1, 6, 12, 52]
print(tri_selection([1, 52, 6, -9, 12]))