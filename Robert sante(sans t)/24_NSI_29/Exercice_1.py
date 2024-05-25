def moyenne(notes: float)-> float:
    length = len(notes)
    val = 0
    coef = 0
    for i in range(length):
        val += notes[i][0] * notes[i][1]
        coef += notes[i][1]
    return val/coef
    

# 12,5
print(moyenne(([(15.0,2),(9.0,1),(12.0,3)])))