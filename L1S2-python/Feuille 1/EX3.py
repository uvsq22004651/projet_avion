"""Exercice 3

    Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Redémarrer” placé en dessous du canevas.
    Diviser la fenêtre en 3 en affichant deux traits verticaux blancs.
    Tant qu’il y a strictement moins de 2 croix, un clic dans la partie gauche affiche une croix bleue inscrite dans un carré de côté 50 centré sur le clic, et sinon ça ne fait rien.
    Tant qu’il y a strictement moins de 3 carrés, un clic dans la partie du milieu affiche un carré vert de côté 50 centré sur le clic, et sinon ça ne fait rien.
    Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
    A tout moment, si l’utilisateur clique sur le bouton “Redémarrer”, alors tous les cercles, les carrés et les croix s’effacent."""

#========================>Imporation de bibliothèques
import tkinter as tk

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constante
size = 600
couleur_fond_canvas='black'
couleur_fond_boutton='darkgreen'
nb_croix = 0
nb_carre = 0 
nb_cercle = 0

#========================>Fonction
def create_geometry(event):
    global nb_croix, nb_carre, nb_cercle
    x = event.x
    y = event.y
    if 0 <= nb_croix < 1 and 0 <= event.x <= 199:
        nb_croix += 1
        canvas.create_line(x-25, y-25, x+25, y+25, fill='blue')
        canvas.create_line(x-25, y+25, x+25, y-25, fill='blue')

    elif 0 <= nb_carre < 2 and 201 <= event.x <= 399:
        nb_carre += 1
        canvas.create_rectangle(x-25, y-25, x+25, y+25, fill='green')
    elif 0 <= nb_cercle < 2 and 401 <= event.x <= 600:
        nb_cercle += 1
        canvas.create_oval(x-25, y-25, x+25, y+25, fill='red')

screen.bind('<Button-1>', create_geometry)

def supprimer():
    global nb_croix, nb_carre, nb_cercle
    for elem in canvas.find_all():
        canvas.delete(elem)
        canvas.create_line((200, 0), (200, 600), fill='white')
        canvas.create_line((400, 0), (400, 600), fill='white')
        nb_croix = 0
        nb_carre = 0 
        nb_cercle = 0

#========================>Programme principal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width = size, height = size, bg = couleur_fond_canvas)
boutton_restart = tk.Button(screen, text = 'Redémarrer',  bg = couleur_fond_boutton, command = supprimer)

canvas.create_line((200, 0), (200, 600), fill='white')
canvas.create_line((400, 0), (400, 600), fill='white')

#========================>Placement widgets
canvas.grid(column = 0, row = 0, columnspan = 3)
boutton_restart.grid(column = 1, row = 1)

#========================>Fin boucle
screen.mainloop()
