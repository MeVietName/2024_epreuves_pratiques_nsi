def parcours_largeur(a)-> list:
    noeuds_list = [a]
    t = []
    # print(noeuds_list)
    while len(noeuds_list) != 0:
        x = noeuds_list.pop(0)
        t.append(x[1])
        if x[0] != None:
            noeuds_list.append(x[0])
        if x[2] != None:
            noeuds_list.append(x[2])
    return t

arbre = ( ( (None, 1, None), 2, (None, 3, None) ),
4, 
( (None, 5, None), 6, (None, 7, None) ) )

print(parcours_largeur(arbre))
# [4, 2, 6, 1, 3, 5, 7]