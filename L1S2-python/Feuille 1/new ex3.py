"""Exercice 3

    Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Redémarrer” placé en dessous du canevas.
    Diviser la fenêtre en 3 en affichant deux traits verticaux blancs.
    Tant qu’il y a strictement moins de 2 croix, un clic dans la partie gauche affiche une croix bleue inscrite dans un carré de côté 50 centré sur le clic, et sinon ça ne fait rien.
    Tant qu’il y a strictement moins de 3 carrés, un clic dans la partie du milieu affiche un carré vert de côté 50 centré sur le clic, et sinon ça ne fait rien.
    Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
    A tout moment, si l’utilisateur clique sur le bouton “Redémarrer”, alors tous les cercles, les carrés et les croix s’effacent."""

import tkinter as tk

windows = tk.Tk()
windows.title('la fenêtre')

def forme(event):
    canvas.create_rectangle((event.x-25, event.y-25), (event.x+25, event.y+25), fill = 'green')

windows.bind("<Button-1>", forme)

canvas = tk.Canvas(windows, width = 400, height = 400, bg = 'black')
canvas.grid(column = 0, row = 1, columnspan = 3)
bouton_creer = tk.Button(windows, text = 'Créer', bg = 'white')
bouton_creer.grid(column = 0, row = 0)

windows.mainloop()