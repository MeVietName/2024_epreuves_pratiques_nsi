# def min_et_max(tab):
#     dictionaire = {"min" : tab[0], "max" : tab[0]}
#     for i in range(len(tab)-1):
#         if tab[i] < tab[i+1]:
#             mini = tab[i]
#             dictionaire.update({"min" : mini})
#         if tab[i] > tab[i+1]:
#             maxi = tab[i]
#             dictionaire.update({"max" : maxi})
#     return dictionaire
# voila ce que j'avais essaye de faire 

# en bas la seconde methode qui MARCHE
    
def min_et_max(tab):
    dictionaire = {"min" : tab[0], "max" : tab[0]}
    for i in range(1, len(tab)):
        if tab[i] < dictionaire['min']:
            dictionaire['min'] = tab[i]
        if tab[i] > dictionaire['max']:
            dictionaire['max'] = tab[i]
    return dictionaire


# {'min': -2, 'max': 9}
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))

# {'min': 0, 'max': 3}
print(min_et_max([0, 1, 2, 3]))

# {'min': 3, 'max': 3}
print(min_et_max([3]))

# {'min': 1, 'max': 3}
print(min_et_max([1, 3, 2, 1, 3]))

# {'min': -1, 'max': -1}
print(min_et_max([-1, -1, -1, -1, -1]))