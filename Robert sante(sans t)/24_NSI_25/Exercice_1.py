def recherche_min(tab: list)-> int:
    length = len(tab)
    minimum = 0
    for i in range(1, length):
        if tab[i] < tab[minimum]:
            minimum = i
    return minimum

# 0
print(recherche_min([5]))

# 2
print(recherche_min([2, 4, 1]))

# 2
print(recherche_min([5, 3, 2, 2, 4]))

# 2
print(recherche_min([-1, -2, -3, -3]))