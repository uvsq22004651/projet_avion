####################
#MIASHS L1S2 TD1
#Groupe 2
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismail AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_incendie
####################

#import
#########################################
#Information liés au groupe
####################
#MIASHS L1S2 TD1
#Groupe 2
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismail AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_incendie

#########################################
#Librairies
import tkinter as tk
import random 

#######################################
#Définitions des constantes
LARGEUR = 1000
HAUTEUR = 2000
TERRAIN = HAUTEUR * LARGEUR
NOMBRE_LIGNE = 10


Racine = tk.Tk()
Racine.title("Projet_Incendie")

Racine.geometry("1080x720")

Canvas1 = tk.Canvas(Racine,bg="grey", width=LARGEUR, height=HAUTEUR)
Canvas1.grid()

########################################
#Variables globales
x = 0
########################################
#Définitions des fonctions
def ligne_horizontale():
    while x<10 :
         Canvas1.create_line(0,NOMBRE_LIGNE*x,HAUTEUR,NOMBRE_LIGNE*x ,fill="Black")
ligne_horizontale()
########################################
#Programme principal







Racine.mainloop()

