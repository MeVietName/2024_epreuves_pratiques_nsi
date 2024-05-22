def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x ...: 
        acc.append(x)
        for y in ...: 
            parcours(adj, ...) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, ...) 
    return acc


# [0, 1, 2, 3]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0))

# [4, 5]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4))
