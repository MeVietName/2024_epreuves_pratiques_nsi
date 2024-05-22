import random

def lancer(n : int)-> list:
    obtenus = []
    for i in range(n):
        obtenus.append(random.randint(1,6))
    return obtenus

def paire_6(tab: list)-> bool:
    count_6 = 0
    for i in tab:
        # print(i)
        if i == 6:
            count_6 += 1
        if count_6 >= 2:
            return True
    return False


# print(paire_6([5, 3, 4]))
print(lancer(5))
# [5, 6, 6, 2, 2]
print(paire_6(lancer(5)))
# True

# print(lancer(5))
# # [6, 5, 1, 6, 6]
# print(paire_6(lancer(5)))
# # True

# print(lancer(3))
# # [2, 2, 6]
# print(paire_6(lancer(3)))
# # False

# print(lancer(0))
# # []
# print(paire_6(lancer(0)))
# # False