def nbr_occurences(chaine: str)-> dict:
    nb = {}
    for i in chaine:
        if i not in nb:
            nb[i] = 1
        else: 
            nb[i] += 1
    return nb 

# {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}
print(nbr_occurences('Hello world !'))

print(nbr_occurences("I like Yến"))