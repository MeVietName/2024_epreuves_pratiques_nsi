# def gb_vers_entier(tab):
#     idk = len(tab)
#     calcul = 0
#     for i in range(idk):
#         if tab[i] == True:
#             calcul += 2**i
#     idk -= 1
#     return calcul
# complique need de le refaire

# Correction :
# def gb_vers_entier(tab):
#     valeur = 0
#     length = len(tab)
#     for i in range(length):
#         verif_bool = tab[length - 1 - i]
#         if verif_bool : 
#             valeur = valeur + 2**i
#     return valeur

# def gb_vers_entier(tab: list)-> int:
#     calcul = 0 
#     n = len(tab)
#     if tab == []:
#         return 0
#     for i in range(n):
#         if tab[i] == True: 
#             calcul += 2**(tab.index(-i))
        
#     return calcul 
            



# 0
print(gb_vers_entier([]))

# 1
print(gb_vers_entier([True]))

# 83
print(gb_vers_entier([True, False, True,False, False, True, True]))

# 130
print(gb_vers_entier([True, False, False, False,False, False, True, False]))