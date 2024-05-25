valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre: 
        return [v] + rendu_glouton(a_rendre - v, rang)
    # v = 1 / [v] = [1] / ca transforme en gros une variable en une liste avec une variable dedans
    else:
        return rendu_glouton(a_rendre, rang + 1) 

# [50, 10, 5, 2]
print(rendu_glouton(67, 0))

# [100, 100, 50, 20, 20, 1]
print(rendu_glouton(291, 0))

# [50, 50, 50, 50, 50, 20, 20, 1]
print(rendu_glouton(291,1)) # si on ne dispose pas de billets de 100