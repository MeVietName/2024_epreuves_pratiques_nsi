# def recherche(elt, tab):
#     for i in tab:
#         if elt == i:
#             return tab.index(i)
#     return None
# Jai fait ce qui est au dessus mais enfaite on peut parcourir la liste avec for i in len de la liste, question pas tres clair

def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i 
    return None


# 2
print(recherche(1, [10, 12, 1, 56]))

# 1
print(recherche(50, [1, 50, 1]))