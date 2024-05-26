from unittest import result


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c 
    return resultat


# 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))

# 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))