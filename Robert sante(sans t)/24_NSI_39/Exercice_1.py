def recherche(elt: int, tab: list)-> int:
    new = None
    for i in range(len(tab)):
        if tab[i] == elt:
            new = i
    return new

 

# None
print(recherche(1, [2, 3, 4]) )

# 2
print(recherche(1, [10, 12, 1, 56]))

# 0
print(recherche(1, [1, 0, 42, 7]))

# 2
print(recherche(1, [1, 50, 1]))

# 5
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))