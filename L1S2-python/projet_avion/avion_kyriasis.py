################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Projet_avion
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
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
    """Création des sièges et du couloir de l'avion"""
    for i in range (7):
        for j in range (30):
            while 1 <= i <= 3:
                canvas.create_rectangle()
################################# PROGRAMME PRINCIPALE 
canvas = tk.Canvas(screen, width = 140, height = 600, bg = "black")


################################# PLACEMENT DES WIDGETS
canvas.grid(column = 0, row = 0)

################################# FIN DE LA BOUCLE
screen.mainloop()
