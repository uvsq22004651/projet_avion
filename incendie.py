################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_incendie
################################

################################# IMPORTATIONS DE LIBRAIRIES

import tkinter as tk 
import random as rd

################################# CONSTANTES
#Création canvas et quadrillage
SIZE = 500
COTE = 10

################################# LISTES

COLOR = ["blue", "forest green", "yellow", "red", "grey", "black"]

################################# FONCTIONS

def quadrillage():
    """Création du quadrillage"""
    x0, x1 = 0, SIZE
    y = 0
    while y <= SIZE:
        canvas.create_line(x0, y, x1, y, fill = "black")
        y += COTE
    
    y0, y1 = 0, SIZE
    x = 0
    while x <= SIZE:
        canvas.create_line(x, y0, x, y1, fill = "black")
        x += COTE



def parcelles():
    """Création des parcelles d'eau, de forêt et de prairie"""
    for i in range(50):
        for j in range(50):
            canvas.create_rectangle(i*COTE, j*COTE, (i+1)*COTE, (j+1)*COTE, fill = (rd.choice(COLOR)))
    return i, j        
        
def voisins(COTE, i, j):
    """Survole toutes les parcelles pour éxaminer leur voisins"""
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
    if a in range(COTE) and b in range(COTE)]


################################# PROGRAMME PRINCIPALE 
racine = tk.Tk()
racine.title("Incendie")

################################
# Création des widgets

canvas = tk.Canvas(racine, width=SIZE, height=SIZE, bg="white", borderwidth=0, highlightthickness=0)
bouton_commencer = tk.Button(racine, text="Création des parcelles", command=parcelles)
bouton_sauvegarder = tk.Button(racine, text="Sauvegarder")
bouton_importer = tk.Button(racine, text='Importer')
bouton_pause = tk.Button(racine, text="Pause")

################################
# Placement des widegts

canvas.grid(column=0, row=1, columnspan=4)
bouton_commencer.grid(column=2, row=2)
bouton_sauvegarder.grid(column=2, row=0)
bouton_importer.grid(column=1, row=0)
bouton_pause.grid(column=1, row=2)

################################
# Fin de la boucle

racine.mainloop()
