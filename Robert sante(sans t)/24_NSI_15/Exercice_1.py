def moyenne(tab):
    length = len(tab)
    val = 0
    for i in tab:
        val += i
    
    return val/length

print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))