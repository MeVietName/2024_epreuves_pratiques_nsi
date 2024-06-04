def voisins_entrants(adj, x: int)-> list:
    uneliste = []
    for i in range(len(adj)):
        for k in adj[i]:
            if x == k:
                uneliste.append(i) # append l'index vue que on cherche a return le sommet(l'index) ayant x comme sommets adjacent 
    return uneliste
    
    
# [2, 3]
print(voisins_entrants([[1, 2], [2], [0], [0]], 0))

# [0]
print(voisins_entrants([[1, 2], [2], [0], [0]], 1))