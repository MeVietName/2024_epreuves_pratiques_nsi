def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1] # 1 du debut
    for i in range(1, len(ligne)): 
        ligne_suiv.append(ligne[i-1] + ligne[i]) # On prend l'index -1 par rapport a celui que l'on veut calculer + celui avec le meme index
    ligne_suiv.append(1) # 1 de fin
    return ligne_suiv 

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle

# [1, 4, 6, 4, 1]
print(ligne_suivante([1, 3, 3, 1]))

# [[1], [1, 1], [1, 2, 1]]
print(pascal(2))

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
print(pascal(3))