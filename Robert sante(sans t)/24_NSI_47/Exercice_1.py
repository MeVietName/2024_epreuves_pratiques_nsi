def max_dico(dico)-> list:
    plus_gros = max(dico.values())
    for i in dico:
        if dico[i] == plus_gros:
            return (i, plus_gros)

# ('Ada', 201)
print(max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }))

# ('Alan', 222)
print(max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }))