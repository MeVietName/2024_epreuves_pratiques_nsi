def ou_exclusif(tab1:list, tab2: list)-> list:
    resultat = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            resultat.append(0)
        else: 
            resultat.append(1)
    return resultat


# [1, 1, 0, 1, 1, 0, 0, 1]
print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))

# [1, 1, 1, 0]
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))
