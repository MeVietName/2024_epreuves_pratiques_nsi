def a_doublon(tab: list)-> bool:
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            return True
    return False

# False
print(a_doublon([]))

# False
print(a_doublon([1]))

# True
print(a_doublon([1, 2, 4, 6, 6]))

# True
print(a_doublon([2, 5, 7, 7, 7, 9]))

# False
print(a_doublon([0, 2, 3]))