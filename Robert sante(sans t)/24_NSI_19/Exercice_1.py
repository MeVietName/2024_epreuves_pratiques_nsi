def liste_puissances(a: int, n: int)-> list:
    liste_calcul = [a]
    for i in range(1, n):
        liste_calcul.append(a*liste_calcul[i-1])
    return liste_calcul
        
def liste_puissances_borne(a: int, borne):
    # if a >= borne: 
    #     return []
    # liste_calcul = [a]
    # calcul = a
    # while calcul < borne:
    #     calcul = calcul * a
    #     if calcul > borne:
    #         return liste_calcul
    #     liste_calcul.append(calcul)
    # return liste_calcul
    if a>=borne:
        return []
    liste = [1]
    i=1
    while a*liste[i-1]<borne:
        liste.append(a*liste[i-1])
        i += 1
    return liste
        

# [3, 9, 27, 81, 243]
print(liste_puissances(3, 5))

# [-2, 4, -8, 16]
print(liste_puissances(-2, 4))

print("--------------")

# [2, 4, 8, 16]
print(liste_puissances_borne(2, 17))

# []
print(liste_puissances_borne(5, 5))