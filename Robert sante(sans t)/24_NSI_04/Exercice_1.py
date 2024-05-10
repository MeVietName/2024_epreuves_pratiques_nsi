def recherche(tab, n):
    index_de_n_dernier = None
    for i in range(len(tab)):
        if tab[i] == n:
            index_de_n_dernier = i
    if index_de_n_dernier == None:
        return index_de_n_dernier
    return index_de_n_dernier
     
     
# None   
# print(recherche([5, 3],1))

# 0
# print(recherche([2,4],2))

# 3
print(recherche([2,3,5,2,4],2))