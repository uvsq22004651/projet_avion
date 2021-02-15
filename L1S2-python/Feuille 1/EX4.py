"""Exercice 4

    Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
    Afficher un carré rempli de rouge de côté 50 au milieu du canevas.
    Si l’utilisateur clique à l’intérieur du carré et que le côté du carré est au moins égale à 20, alors le côté du carré diminue de 10 (effacer et réafficher).
    Si l’utilisateur clique à l’extérieur du carré et que le côté du carré est au plus égal à 100, alors le côté du carré augmente de 10 (effacer et réafficher).
    Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie plus le carré) et le nom du bouton devient “Restart”.
    Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”."""

#========================>Imporation de bibliothèques
import tkinter as tk

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constante
size = 500
PETITE_COORDONNEE = 225
GRANDE_COORDONNE = 275
couleur_fond_canvas = 'white'
couleur_fond_boutton = 'darkgreen'

#========================>Fonction
def reduction(event):
    global PETITE_COORDONNEE, GRANDE_COORDONNE
    for elem in canvas.find_all():
        canvas.delete(elem)
    if PETITE_COORDONNEE <= event.x <= GRANDE_COORDONNE and PETITE_COORDONNEE <= event.y <= GRANDE_COORDONNE and GRANDE_COORDONNE - PETITE_COORDONNEE >= 20:
        print('inside')
  
        canvas.create_rectangle((PETITE_COORDONNEE + 5, PETITE_COORDONNEE + 5), (GRANDE_COORDONNE - 5, GRANDE_COORDONNE - 5), fill = 'red')
        print(PETITE_COORDONNEE, GRANDE_COORDONNE)
    


screen.bind('<Button-1>', reduction)

#========================>Programme principal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width = size, height = size, bg = couleur_fond_canvas)
boutton_pause = tk.Button(screen, text = 'Pause', bg = couleur_fond_boutton)
canvas.create_rectangle((PETITE_COORDONNEE-10, PETITE_COORDONNEE-10), (GRANDE_COORDONNE, GRANDE_COORDONNE), fill = 'red')

#========================>Placement widgets
canvas.grid(column = 0, row = 0, columnspan = 3)
boutton_pause.grid(column = 1, row = 1)

#========================>Fin boucle
screen.mainloop()