def compte_occurrences(x, tab: list)-> int:
    count = 0 
    for i in tab:
        if i == x: 
            count += 1
            
    return count 

# 0
print(compte_occurrences(5, []))

# 1
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))

# 3
print(compte_occurrences('a', ['a','b','c','a','d','e','a']))