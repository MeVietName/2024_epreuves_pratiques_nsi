def max_et_indice(tab):
    length = len(tab)
    comparateur = tab[0]
    # ["valeur", "index"]
    idk = [tab[0], 0]
    
    for i in range(length):
        print("for")
        if comparateur < tab[i]:
            comparateur = tab[i]
            idk[0] = tab[i]
            idk[1] = i
            print("if")
    return idk
        



# 9, 3
print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))

# -2, 0 
# print(max_et_indice([-2]))

# 3, 2
# print(max_et_indice([-1, -1, 3, 3, 3]))