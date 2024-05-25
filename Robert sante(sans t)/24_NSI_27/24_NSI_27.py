def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j+1 < len(M): # propage en haut 
        colore_comp1(M, i, j+1, val) 
    if j-1 >= 0: # propage en bas 
        colore_comp1(M, i, j-1, val)
    return M


# [[0, 0, 1, 0], 
# [0, 3, 0, 1], 
# [3, 3, 3, 0], 
# [0, 3, 3, 0]]
M = [[0, 0, 1, 0], 
     [0, 1, 0, 1], 
     [1, 1, 1, 0], 
     [0, 1, 1, 0]]

resultat = colore_comp1(M, 2, 1, 3)

for i in resultat:
    print(i)
