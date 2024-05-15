def nombre_de_mots(phrase: str) -> int:
    count = 1
    length = len(phrase)
    for i in range(0, length):
        if phrase[i] in ['.','!','?']:
            # Merci kant1 
            # If phrase[i] == trux1 OR phrase[i] == truc2
            # if phrase[i] in [., !, ?]
            return count
        elif phrase[i] == ' ' and phrase[i+1] not in ['!','?']:
            count += 1
    return count
        


# 4
print(nombre_de_mots('Cet exercice est simple.'))

# 6
print(nombre_de_mots('Le point d exclamation est séparé !'))

# 10
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))

# 1
print(nombre_de_mots('Fin.'))