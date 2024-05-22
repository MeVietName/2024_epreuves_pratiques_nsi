def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return "0"
    bin_a = "" 
    while a > 0:
        # print(bin_a)
        bin_a = str(a%2) + bin_a
        # print(a)
        a = a//2
    return bin_a

# BIEN SE RAPPELER : 
# print(3//2)   >> 1
# print(3/2)    >> 1.5



# '1010011'
print(binaire(83))

# '110'
print(binaire(6))

# '1111111'
# print(binaire(127))

# '0'
# print(binaire(0))