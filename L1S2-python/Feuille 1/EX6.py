"""Exercice 6

    Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Annuler” placé à gauche du canevas.
    Afficher en haut à gauche du canevas 3 carrés juxtaposés de côté 50 et de couleur verte jaune et bleu.
    Afficher un cercle noir de rayon 50 au centre du canevas.
    Si l’utilisateur clique dans un des carrés du bas, le cercle prend la couleur du carré sur lequel l’utilisateur a cliqué.
    Si l’utilisateur clique en dehors des carrés alors le cercle devient noir.
    Si l’utilisateur clique sur le bouton “Annuler” alors le cercle reprend la couleur qu’il avait avant le dernier changement de couleur. Il doit être possible d’annuler tous les 
    changements de couleur jusqu’au début."""

#========================>Imporation de bibliothèques
import tkinter as tk 

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constante
size = 500
couleur_fond_canvas = 'white'
couleur_fond_boutton = 'darkgreen'
carre1_color = 'green'
carre2_color = 'yellow'
carre3_color = 'blue'

#========================>Fonction
def color_change(event):
    if 0 <= event.x <= 50 and 0 <= event.y <= 50:
        canvas.itemconfigure(cercle, fill = carre1_color)
    elif 51 <= event.x <= 101 and 0 <= event.y <= 50:
        canvas.itemconfigure(cercle, fill = carre2_color)
    elif 102 <= event.x <= 152 and 0 <= event.y <= 50:
        canvas.itemconfigure(cercle, fill = carre3_color)
    elif event.x>152 or (event.x<152 and event.y>50):
        canvas.itemconfigure(cercle, fill = 'black')

screen.bind('<Button-1>', color_change)


#========================>Programme principal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width = size, height = size, bg = couleur_fond_canvas)
boutton_annul = tk.Button(screen, text = 'Annuler', width=50, bg = couleur_fond_boutton)

carre1 = canvas.create_rectangle((0, 0), (50, 50), fill = carre1_color)
carre2 = canvas.create_rectangle((51, 0), (101, 50), fill = carre2_color)
carre3 = canvas.create_rectangle((102, 0), (152, 50), fill = carre3_color)

cercle = canvas.create_oval((225, 225), (275, 275), fill = 'black')

#========================>Placement widgets
canvas.grid(column = 0, row = 0, rowspan = 3)
boutton_annul.grid(column = 2, row = 1)

#========================>Fin boucle
screen.mainloop()
