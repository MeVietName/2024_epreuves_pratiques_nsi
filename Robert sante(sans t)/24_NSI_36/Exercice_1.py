def occurrences(caractere, chaine):
    count = 0
    for i in chaine:
        if caractere == i:
            count += 1
    return count

# 2
print(occurrences('e', "sciences"))

# 4
print(occurrences('i',"mississippi"))

# 0
print(occurrences('a',"mississippi"))