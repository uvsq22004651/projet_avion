########################
# Auteurs:
# Pierre Coucheney
# Toto Lehéro
# ...
# Groupe de TD:
# MPCI 5
########################

########################
# import des librairies
import tkinter as tk


########################
# Constantes

COULEUR_FOND = "grey100"
LARGEUR = 600
HAUTEUR = 400
COTE = 100
NB_COL = LARGEUR//COTE
NB_LINE = HAUTEUR//COTE
COULEUR_VIVANT = 'yellow'
COULEUR_VIVANT = 'black'
########################
# Variables globales








########################
# fonctions
def quadrillage():
    """Affiche un quadrillage sur le canvas"""
    global canvas, LARGEUR, HAUTEUR
    """Affiche un quadrillage sur le canvas."""
    for l in range(0,601,10):
        for h in range(0,401,10):
            canvas.create_line((0, h), (LARGEUR, h), fill = 'black')
            canvas.create_line((l, 0), (l, HAUTEUR), fill = 'black')


def coords_to_lg(x, y):
    """Fonctiojn qui retourne la colonne et la ligne du quadrillage à partir des coordonnées x et y"""
    return x//COTE, y//COTE

def chnage_carre(event):
    """Change l'état du carré sur lequel on a cliqué"""
    i, j = coords_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i +COTE, j*COTE
        carre = canvas.create_rectangle(x, y, X + COTE, y + COTE, fill = COULEUR_VIVANT, outline = COULEUR_QUADR)


def creer_tableau():
    """Initialiser un tableau à deuxx dimensions qui vaut -1 partout
    -1 est une case morte
    identifiant du carré dessiné si une case est vivante
    tableau[i][j] est la valeur de la case à la colonne i et la ligne j
    """
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1]*NB_LINE)
    tableau = [tableau_col for i in range (NB_COL)]
    print(tableau)



########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
quadrillage()
# placement des widgets
canvas.grid(row=0)
# boucle principale
racine.mainloop()
