#script to create folder contained : pdf + .py
import os
import shutil
import glob
 
os.chdir("les copies")
file_list = os.listdir()
print(file_list)
os.chdir("..")
os.listdir()

#directory name : 24_NSI_<nb>
for i in range(47):
    target_folder = file_list[i]
    folder_name = target_folder.replace(".pdf", " ") #permet d'enlever l'extension dans le nom du fichier
    print(folder_name)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    print(folder_name)
    #need to fix the path to move 
    shutil.move(file_list[i], folder_name)
    shutil.move(file_list[i+1], folder_name)
    i=+1
    
    


# os.makedirs(nom_du_fichier, )
source_file = "D:\Programmes\2024_epreuves_pratiques_nsi"

destination_file = "D:\Programmes"


# https://note.nkmk.me/en/python-str-remove-strip/#remove-exact-match-string-replace