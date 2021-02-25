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
# Couleur des parcelles
EAU="blue"
FORET="green"
PRAIRIE="yellow"
FEU="red"
CENDRES_TIEDES="grey"
CENDRES_ETEINTES="black"

#Création canvas et quadrillage
LARGEUR = 600
HAUTEUR = 400
COTE = 25

################################# LISTES

color_liste = [EAU, FORET, PRAIRIE]

################################# FONCTIONS

def quadrillage():
    """Création du quadrillage"""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill = "black")
        y += COTE
    
    y0, y1 = 0, HAUTEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill = "black")
        x += COTE


def parcelles():
    """Création des parcelles d'eau, de forêt et de prairie"""
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    for parcelle in range(384):
        canvas.create_rectangle(x0, y0, x1, y1, fill = rd.choice(color_liste))
        x0 += COTE
        x1 += COTE
        if x0 == LARGEUR:
            x0 = 0
            y0 += COTE
            x1 = COTE
            y1 += COTE
            canvas.create_rectangle(x0, y0, x1, y1, fill = rd.choice(color_liste))


################################# PROGRAMME PRINCIPALE 
racine = tk.Tk()
racine.title("Incendie")

################################
# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="white", borderwidth=0, highlightthickness=0)
bouton_commencer = tk.Button(racine, text="Création des parcelles", command=lambda:[quadrillage(), parcelles()])
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
