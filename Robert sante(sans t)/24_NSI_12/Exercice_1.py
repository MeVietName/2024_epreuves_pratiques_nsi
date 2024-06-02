def tri_selection(tab: list)-> list:
    for i in range(len(tab)):
        compa = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[compa]:
                compa = j
        tab[i], tab[compa] = tab[compa], tab[i]
        
    return tab
            
            
        

# [-9, 1, 6, 12, 52]
print(tri_selection([1, 52, 6, -9, 12]))