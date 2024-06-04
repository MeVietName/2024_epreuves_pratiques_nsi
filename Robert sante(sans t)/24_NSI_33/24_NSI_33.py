def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers

print(crible(40))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(crible(5))
# [2, 3]

# 0       False
# 1       False
# 2       False
# 3       True
# 4       False
# 5       True
# 6       False
# 7       True
# 8       False
# 9       False
# 10      False
# 11      True
# 12      False
# 13      True
# 14      False
# 15      False
# 16      False
# 17      True
# 18      False
# 19      True
