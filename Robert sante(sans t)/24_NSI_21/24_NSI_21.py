def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj: 
            parcours(adj, x, accessibles(adj, y)) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc


# [0, 1, 2, 3]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0))

# [4, 5]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4))
