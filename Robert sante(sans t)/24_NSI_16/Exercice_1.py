def ecriture_binaire_entier_positif(n: int)-> str:
    if n == 0:
            return "0"
    binaire = ""
    while n > 0: 
        binaire = str(n%2) + binaire
        n = n//2
    return binaire

# '0'
print(ecriture_binaire_entier_positif(0))

# "10"
print(ecriture_binaire_entier_positif(2))

# "1101001"
print(ecriture_binaire_entier_positif(105))