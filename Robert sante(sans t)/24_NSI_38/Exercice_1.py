def indices_maxi(tab: list)-> list:
    le_max = max(tab)
    where = []
    for i in range(len(tab)):
        if tab[i] == le_max: 
            where.append(i)    
    return (le_max, where)

# (9, [3, 8])
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))

# (7, [0])
print(indices_maxi([7]))