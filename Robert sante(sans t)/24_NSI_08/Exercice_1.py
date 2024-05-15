def delta(liste: list) -> list:
    length = len(liste)
    comp = [liste[0]]
    for i in range(length-1):
        comp.append(liste[i+1]-liste[i])
    return comp
        
            
    
    
# 1000, -200, 2, 198, 3]
print(delta([1000, 800, 802, 1000, 1003]))

# [42]
print(delta([42]))