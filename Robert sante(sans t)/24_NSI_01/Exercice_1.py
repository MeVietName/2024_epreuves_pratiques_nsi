a = {'F':['B','G'], 
     'B':['A','D'], 
     'A':['',''], 
     'D':['C','E'], 
     'C':['',''], 
     'E':['',''], 
     'G':['','I'], 
     'I':['','H'], 
     'H':['','']}

# cor
def taille(arbre, lettre):
     if lettre == '':
          return 0
     return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

print(taille(a, "F"))

'''
------- J'ai essaye ca -----
count = 0

def taille(arbre: dict, lettre: str, compteur: int):
     if arbre[lettre][0] != "":
          taille(arbre, arbre[lettre][0], compteur)
          return count + 1
          print("if1")
          print(count)
          # return countgauche
          
     if arbre[lettre][1] != "":
          taille(arbre, arbre[lettre][1], compteur)
          return count + 1
          print("if2")
          print(count)
          # return countdroite

     print("TOTAL COUNT : ")
     total = count + 1
     print(count)
     
     return taille(arbre, lettre, compteur)


BIGTOTALCOUNT = taille(a, "F", count)
print(f"taille count {taillecount}")


# taillecount = 0
# taillecount += taille(a, "F")
# print(f"taille count {taillecount}")
          
# need de trouver comment faire le compteur et de faire le return

     


# test = a["B"]
# print(test)
# print(test[0])
# or
# print(a["F"][0])
'''