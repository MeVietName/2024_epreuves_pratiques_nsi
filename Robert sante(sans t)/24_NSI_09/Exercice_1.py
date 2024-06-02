def effectif_notes(tab: list)-> list:
    new = [0] * 11
    for i in tab:
        new[i] += 1
        
    return new
    
    
    
# [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
print(effectif_notes([2, 0, 5, 9, 6, 9, 10, 5, 7,
9, 9, 5, 0, 9, 6, 5, 4]))


# [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
print(print(effectif_notes([2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1])))