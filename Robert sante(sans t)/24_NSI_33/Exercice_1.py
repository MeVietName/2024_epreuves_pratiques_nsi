def renverse(mot: str)-> str:
    new = ""
    i = -1 
    while len(mot) != len(new):
        new += mot[i]
        i += -1
    return new
    
        

# ""
print(renverse(""))

# "cba"
print(renverse("abc"))

# "euqitamrofni"
print(renverse("informatique"))