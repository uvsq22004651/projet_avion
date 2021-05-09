################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Projet_avion
#Yannis KYRIASIS
#Nadir HADIOUI
#Ismael AYAD
#Oumou ATJI
#Nabil SABER
#https://github.com/uvsq22004651/projet_avion/edit/main/incendie.py
################################

################################ Fonctionnement du programme
"""Ce code est une simulation de passager ce plaçant à une place qui leur est 
attribué à bord d'un avion. Si deux passager sont l'un derrière l'autre, le premier 
dans le couloir de l'avion, le premier doit attendre que le second se soit placé à sont
siège. Chaque passager à 0,1 ou 2 bagages"""

################################# IMPORTATIONS DE LIBRAIRIES
import tkinter as tk

################################ INITIALISATION
screen = tk.Tk()
screen.title("Simulation avion")

################################# CONSTANTES
SIEGES_VIDES = "steel blue"
COULOIR = "light steel blue"
ZERO_BAGAGE = "yellow"
UN_BAGAGE = "orange"
DEUX_BAGAGES = "red"
SIEGES_OCCUPEES = "green"
LARGEUR = 140
HAUTEUR = 600
# la longeur des carrés qui constituent le quadrillage
COTE = 20
NB_COl = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

tableau = None
coords = None
cpt = 0

################################# FONCTIONS
def sieges_couloir():
    global COTE, SIEGES, COULOIR
    """Création des sièges de l'avion et du couloir de l'avion"""
    for i in range (7):
        for j in range (30):
                celule = canvas.create_rectangle(i*COTE, j*COTE, (1+i)*COTE, (1+j)*COTE, fill = SIEGES)
                if i == 3:
                    canvas.itemconfig(celule, fill = COULOIR)


def coordonnees_sieges():
    """Acrédite une coordonnées à chaques sièges de l'avion sous forme
    de tableau à deux dimensions"""
    coordonnées = []
    for col in range (1,4):
        for line in range (1,31):
            coordonnées.append([col, line]) #sièges à gauche du couloir
    for col in range (4, 8):
        for line in range (1, 31):
            coordonnées.append([col, line]) #sièges à droite du couloir 


def tableau_2D():
    """Création d'un tableau à deux dimension permettant de connaître
    le rôle de chaque celule, le couloir est initilisé à 0, tandis 
    que les sièges sont initialisés à 1"""
    global tableau
    tableau = []
    for i in range(NB_COl):
        if i == 3:
            tableau.append([0]*NB_LINE) #couloir
        else:
            tableau.append([1]*NB_LINE) #sièges


def voisins_couloir(i, j):
    """Examine le couloir de l'avion pour pour examiner leur voisins"""
    cpt = 0
    for v in range(3, 4):
        for w in range(NB_LINE):
            if tableau[v][w] != 0 and [v, w] != [i, j]:
                cpt += 1
    return cpt


def traite_case_couloir(i, j):
    """Traite la case à la colonne i et ligne j en retournant la nouvelle 
    valeur du tableau"""
    nb_vivant = compte_vivant(i, j)
    if tableau[i][j] == -1:


def voisins_sièges():
    """Examine les sièges pour savoir si un passager est déjà placé"""

################################# PROGRAMME PRINCIPALE 
canvas = tk.Canvas(screen, width = 280, height = 600, borderwidth=0, highlightthickness=0, bg = "black")
sieges_couloir()


################################# PLACEMENT DES WIDGETS
canvas.grid(column = 0, row = 0, rowspan=5)


################################# FIN DE LA BOUCLE
screen.mainloop()
