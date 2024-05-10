def maximum_tableau(tab):
    return max(tab)

print(maximum_tableau([85, 173, 20, 1, 18]))

'''
Ca marche mais je sais pas si ca va passer ce pendant voila la correction

def maximum_tableau(tab):
    vmax = tab[0]
    for v in tab:
        if v > vmax:
            vmax = v
    return vmax
'''