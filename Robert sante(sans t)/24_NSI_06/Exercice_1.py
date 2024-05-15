def verifie(tab):
    length = len(tab)
    # dans la correction il avait rajouter ca mais bon
    # if n < 2 :
    #     return True
    for i in range(0, length-1):
        print(i, i+1)
        if tab[i] > tab[i+1]:
            return False
    return True

# True
# print(verifie([0, 5, 8, 8, 9]))

# False
# print(verifie([8, 12, 4]))

# True
# print(verifie([-1, 4]))

# True
# print(verifie([]))

# True
# print(verifie([5]))