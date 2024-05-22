def ecriture_binaire_entier_positif(n: int)-> str:
    if n == 0:
            return "0"
    binaire = ""
    while n > 0: 
        binaire = str(n%2) + binaire
        n = n//2
    return binaire

'''
Correction :
def ecriture_binaire_entier_positif(n):
    vbin = str(n%2)
    n = n // 2
    while n > 0:
        vbin = str(n%2) + vbin
        n = n //2
    return vbin
'''


# '0'
print(ecriture_binaire_entier_positif(0))

# "10"
print(ecriture_binaire_entier_positif(2))

# "1101001"
print(ecriture_binaire_entier_positif(105))