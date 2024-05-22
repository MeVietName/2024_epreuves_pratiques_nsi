def liste_puissances(a : int, n : int)-> list:
    resultat_liste = [a]
    for i in range(1, n):
        resultat_liste.append(a*resultat_liste[i-1])
    return resultat_liste
    



# [3, 9, 27, 81, 243]
print(liste_puissances(3, 5))

# [-2, 4, -8, 16]
print(liste_puissances(-2, 4))

# [2, 4, 8]
print(liste_puissances(-2, 4))

# # [2, 4, 8, 16]
# print(liste_puissances_borne(2, 17))

# # []
# print(liste_puissances_borne(5, 5))