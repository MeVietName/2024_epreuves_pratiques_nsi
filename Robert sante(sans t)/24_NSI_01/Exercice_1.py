a = {'F':['B','G'], 
     'B':['A','D'], 
     'A':['',''], 
     'D':['C','E'], 
     'C':['',''], 
     'E':['',''], 
     'G':['','I'], 
     'I':['','H'], 
     'H':['','']}


def taille(arbre: dict, lettre: str):
     countgauche = 0
     countdroite = 0
     if arbre[lettre][0] != "":
          taille(arbre, arbre[lettre][0])
          countgauche += 1
          print(countgauche)
          print("if1")
          
     if arbre[lettre][1] != "":
          taille(arbre, arbre[lettre][1])
          countdroite += 1
          print(countdroite)
          print("if2")

     total = countgauche + countdroite
     print(f"le total est {total}")
     return total

taillecount = 0
taillecount += taille(a, "F")
print(f"taille count {taillecount}")
          
# need de trouver comment faire le compteur et de faire le return

     


# test = a["B"]
# print(test)
# print(test[0])
# or
# print(a["F"][0])