def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse

def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        oui = pile.pop()
        if oui >= 0: 
            pile_positifs.append(oui)
    return renverse(pile_positifs)

# [5, 4, 3, 2, 1]
print(renverse([1, 2, 3, 4, 5]))

# [0, 5, 4, 10, 9]
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))

# []
print(positifs([-2]))