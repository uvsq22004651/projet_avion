################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Projet_avion
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_avion/edit/main/incendie.py
################################

################################ Fonctionnement du programme


################################# IMPORTATIONS DE LIBRAIRIES
import tkinter as tk

################################ INITIALISATION
screen = tk.Tk()

################################# CONSTANTES
SIEGES = "steel blue"
COULOIR = "light steel blue"
ZERO_BAGEGE = "yellow"
UN_BAGAGE = "orange"
DEUX_BAGAGES = "red"
PLACE = "green"
LARGEUR = 140
HAUTEUR = 600
# la longeur des carrés qui constituent le quadrillage
COTE = 20
NB_COl = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

################################# FONCTIONS
def sieges_couloir():
    global COTE, SIEGES, COULOIR
    """Création des sièges et du couloir de l'avion"""
    for i in range (7):
        for j in range (30):
                carré = canvas.create_rectangle(i*COTE, j*COTE, (1+i)*COTE, (1+j)*COTE, fill = SIEGES)
                if i == 3:
                    canvas.itemconfig(carré, fill = COULOIR)

def coordonnées():
    """Création des coordonnées des sièges des passagers"""

################################# PROGRAMME PRINCIPALE 
canvas = tk.Canvas(screen, width = 140, height = 600, borderwidth=0, highlightthickness=0, bg = "black")
sieges_couloir()


################################# PLACEMENT DES WIDGETS
canvas.grid(column = 0, row = 0)

################################# FIN DE LA BOUCLE
screen.mainloop()
