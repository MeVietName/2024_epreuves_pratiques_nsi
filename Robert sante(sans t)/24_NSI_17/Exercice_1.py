def nb_repetitions(elt, tab: list):
    compteur = 0
    for i in tab:
        if elt == i:
            compteur += 1
    return compteur

# 3
print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))

# 2
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))

# 0
print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))