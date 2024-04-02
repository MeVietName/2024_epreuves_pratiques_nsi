#script to create folder contained : pdf + .py
import os
import shutil

def padding(entree: int, nbre_caracteres: int):
    entree_str = str(entree)
    while len(entree_str) < nbre_caracteres:
        entree_str = "0" + entree_str
    return entree_str

# directory name : 24_NSI_<nb>
for i in range(1, 49):
    num = padding(i, 2)
    folder_name = "24_NSI_" + num
    print(folder_name)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    print(folder_name)
    #need to fix the path to move 
    shutil.move("les copies/24_NSI_" + num + ".pdf" , folder_name)
    shutil.move("les copies/24_NSI_" + num + ".py" , folder_name)



# https://note.nkmk.me/en/python-str-remove-strip/#remove-exact-match-string-replace