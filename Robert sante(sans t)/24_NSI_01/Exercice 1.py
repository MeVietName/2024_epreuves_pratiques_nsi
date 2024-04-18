a = {'F':['B','G'], 
     'B':['A','D'], 
     'A':['',''], 
     'D':['C','E'], 
     'C':['',''], 
     'E':['',''], 
     'G':['','I'], 
     'I':['','H'], 
     'H':['','']}



def taille(arbre, lettre -> str):
     if arbre[lettre][0] != None:
          taille(arbre, arbre[lettre][0])
          
     if arbre[lettre][1] != None:
          taille(arbre, arbre[lettre][1])
          
taille(a, "F")
          
# il faudrait tester pour voir si ca marche et ce qui faut changer, et aussi reflechir a comment faire un compteur de noeud pour return la taille 
          


     

     


# test = a["B"]
# print(test)
# print(test[0])

# print(a["F"][0])