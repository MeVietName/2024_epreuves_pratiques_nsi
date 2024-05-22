def recherche_motif(motif, texte)-> list:
    resultat = []
    length = len(texte)
    for i in range(length-1):
        # print(i)
        if texte[i] == motif[0]:
            if texte[i+1] == motif[1]:
                resultat.append(i)
    return resultat

print(recherche_motif("ab", ""))
# []

print(recherche_motif("ab", "cdcdcdcd"))
# []

print(recherche_motif("ab", "abracadabra"))
# [0, 7]

print(recherche_motif("ab", "abracadabraab"))
# [0, 7, 11]