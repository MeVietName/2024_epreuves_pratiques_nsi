def min_et_max(tab: list)-> dict:
    dictionaire = {}
    minimum, maximum = tab[0], tab[0]
    for i in range(1, len(tab)):
        if tab[i] > maximum:
            maximum = tab[i]
        if tab[i] < minimum:
            minimum = tab[i]
    dictionaire["min"] = minimum
    dictionaire["max"] = maximum
    return dictionaire


# {'min': -2, 'max': 9}
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))

# {'min': 0, 'max': 3}
print(min_et_max([0, 1, 2, 3]))

# {'min': 3, 'max': 3}
print(min_et_max([3]))

# {'min': 1, 'max': 3}
print(min_et_max([1, 3, 2, 1, 3]))

# {'min': -1, 'max': -1}
print(min_et_max([-1, -1, -1, -1, -1]))