def ajoute_dictionnaires(d1, d2)-> dict:
    d = d1.copy()
    length_un = len(d1)
    length_deux = len(d2)
    
    for i in d2:
        if i in d:
            d[i] = d[i] + d2[i]
        if i not in d:
            d[i] = d2[i]
            
    return d

            
            
            
# {1: 5, 2: 16, 3: 11}
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))

# {2: 9, 3: 11}
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))

# {1: 5, 2: 7}
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

git config --global user.email "thibautnemo@gmail.com"
git config --global user.name "MeVietName"