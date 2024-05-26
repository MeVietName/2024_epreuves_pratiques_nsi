def recherche(tab: list, n: int)-> int:
    if n not in tab: 
        return None
    return tab.index(n)
    

# 3
print(recherche([2, 3, 4, 5, 6], 5))

# None
print(recherche([2, 3, 4, 6, 7], 5)) # renvoie None