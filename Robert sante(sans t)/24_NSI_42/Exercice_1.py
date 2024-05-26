def moyenne(tab: list)-> float:
    a = 0
    for i in tab:
        a += i 
    return a/len(tab)

# 1.0
print(moyenne([1]))
# 4.0
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
# 1.5
print(moyenne([1, 2]))
