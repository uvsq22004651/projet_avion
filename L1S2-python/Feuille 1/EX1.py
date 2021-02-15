"""Exercice 1
    Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
    Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
    A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
    Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
    A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné."""

#========================>Imporation de bibliothèques
import tkinter as tk

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constantes
size = 500
nb_clic = 0
couleur_fond_canvas = 'black'
couleur_fond_boutton = 'darkgreen'
couleur_fond_rectangle = 'red'

#========================>Fonctions
def clic(event):
    """Changement de couleur du rectangle lorsque l'on clic dessus"""
    global nb_clic, couleur_fond_rectangle
    x = event.x
    y = event.y
    if (200 <= x <= 300 and 225 <= y <= 275) and nb_clic == 0:
        nb_clic += 1
        couleur_fond_rectangle = 'blue'
        canvas.create_rectangle((300, 275), (200, 225), fill=couleur_fond_rectangle)
    elif (200<=x<=300 and 225<=y<=275) and nb_clic==1:
        nb_clic = 0
        couleur_fond_rectangle = 'red'
        canvas.create_rectangle((300, 275), (200, 225), fill=couleur_fond_rectangle)
    else:
        (x<199 or x<301) and (y<224 or y<276)
        nb_clic=2

screen.bind("<Button-1>", clic) 

def reinisialiser():
    global nb_clic, couleur_fond_rectangle
    nb_clic = 0
    couleur_fond_rectangle = 'red'    

#========================>Programme pricipal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width=size, height=size, bg=couleur_fond_canvas)
button_restart = tk.Button(screen, text = 'Recommencer', bg=couleur_fond_boutton, command=reinisialiser)
rectangle = canvas.create_rectangle((300, 275), (200, 225), fill=couleur_fond_rectangle)

#========================>Placement widget
canvas.grid(column = 0, row=0, columnspan=3)
button_restart.grid(column=1, row=1)

#========================>Fin boucle
screen.mainloop()