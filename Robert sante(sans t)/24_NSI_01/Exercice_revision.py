a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre: dict, lettre: str)-> int:
    if lettre == "":
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
    
print(taille(a, 'F'))
# 9
print(taille(a, 'B'))
# 5
print(taille(a, 'I'))
# 2