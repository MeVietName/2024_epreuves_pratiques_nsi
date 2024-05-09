# – True si on peut obtenir mot en remplaçant convenablement les caractères '*' de mot_a_trous ;
# – False sinon.

# mot = VIETNAM
# mot_a_trous = V**TN*M

def idk(mot, mot_a_trous):
    longueur = len(mot_a_trous)
    motlongueur = len(mot)
    if longueur != motlongueur:
            return False
    for i in range(0, longueur-1):
        if mot[i] != mot_a_trous[i]:
            if mot_a_trous[i] != "*":
                return False
    return True


print(idk("VIETNAM", "V**TN*M"))




    # for i in mot:
    #     for k in range(0, longueur-1):
    #         if mot_a_trous[k] == i:
    #             print("if")
    #             break
    #         else: 
    #             print("else")
    #             break
    

test string index
# test = "text"
# print(test[0])