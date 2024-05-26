def enumere(tab: list)-> dict:
    oui = {}
    for i in range(len(tab)):
        if tab[i] not in oui:
            oui[tab[i]] = [i]
        else:
            oui[tab[i]].append(i)
    return oui

# {}
print(enumere([]))

# {1: [0], 2: [1], 3: [2]}
print(enumere([1, 2, 3]))

# {1: [0, 1, 5], 2: [2, 4], 3: [3]}
print(enumere([1, 1, 2, 3, 2, 1]))