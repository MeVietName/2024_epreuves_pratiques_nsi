animaux = [ 
{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def selection_enclos(tab: list, num_enclos: int)-> list: 
    resultat = []
    for i in range(len(tab)):
        if tab[i]['enclos'] == num_enclos:
            resultat.append(tab[i])
    return resultat
    
    
# [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
# {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
print(selection_enclos(animaux, 5))

# [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
print(selection_enclos(animaux, 2))

# []
print(selection_enclos(animaux, 7))