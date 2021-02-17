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
FEU="red"
PRAIRIE="yellow"
CENDRES_TIEDES="grey"
CENDRES_ETEINTES="black"


################################# LISTES

color_liste = [EAU, FORET, FEU, PRAIRIE, CENDRES_TIEDES, CENDRES_ETEINTES]


################################# FONCTIONS

def quadrillage():
    """Création du quadrillage"""
    for l in range(0, 601, 10):
        for h in range(0, 401, 10):
            canvas.create_line((0, h), (600, h), fill='black')
            canvas.create_line((l, 0), (l, 400), fill='black')



################################# PROGRAMME PRINCIPALE 
racine = tk.Tk()
racine.title("Incendie")


################################
# Création des widgets

canvas = tk.Canvas(racine, width=600, height=400, bg="white")
bouton_commencer = tk.Button(racine, text="Commencer", command=quadrillage)
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

#MARGES
canvas.create_line(0,2,600,2)
canvas.create_line(2,400,2,0)

################################
# Fin de la boucle

racine.mainloop()
