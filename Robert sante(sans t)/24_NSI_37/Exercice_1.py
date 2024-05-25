def moyenne(tab: list)-> int:
    resultat = 0
    
    # Premiere solution : 
    # assert tab == [], "Le tableau est vide veuillez entrez des notes"
    # Deuxieme solution :
    if tab == []:
        return "Le tableau est vide veuillez entrez des notes"
    
    for i in tab:
        resultat += i 
    return resultat/len(tab)

# 5.333333333333333
print(moyenne([5,3,8]))

# 5.5
print(moyenne([1,2,3,4,5,6,7,8,9,10]))

# Comportement différent suivant le traitement proposé.
print(moyenne([]))
