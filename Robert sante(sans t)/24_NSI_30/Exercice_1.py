def fusion(tab1: list, tab2: list)-> list:
    okay = tab1 + tab2
    okay.sort()
    return okay


# [2, 3, 5, 5]
print(fusion([3, 5], [2, 5]))

# [-3, -2, 4, 5, 10]
print(fusion([-2, 4], [-3, 5, 10]))

# [2, 4, 6]
print(fusion([4], [2, 6]))

# []
print(fusion([], []))

# [1, 2, 3]
print(fusion([1, 2, 3], []))