def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: 
        return str(r)
    else:
        return dec_to_bin(q) + str(r) 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1 #car juste en haut on verifie si c'est un 0, si oui bit_droit = 0, vu qu'il n'y a que des 0,1 alors si pas 0 alors 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit 
    # on met 2 par ce que *2
    
    
    
    
    
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return r
    else:
        return dec_to_bin(q) + r
    
def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
                bit_droit = 0
            else:
                bit_droit = 1
    return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

# '11001'
print(dec_to_bin(25))

# 42
print(bin_to_dec('101010'))