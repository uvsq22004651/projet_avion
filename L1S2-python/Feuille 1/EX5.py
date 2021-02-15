"""Exercice 5

    Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 600x600 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
    Afficher deux lignes verticales séparant le canevas en trois parties égales. Celle de gauche est rouge, et celle de droite est bleu.
    A chaque fois que l’utilisateur clique sur le canevas, les lignes verticales se déplacent de 10 pixels vers l’endroit cliqué: par exemple si le clic est entre les deux lignes, celle de 
    gauche se déplace vers la droite, et celle de droite se déplace vers la gauche. De plus, les couleurs des lignes sont échangées.
    Si l’utilisateur clique sur le bouton “Recommencer”, alors les 2 lignes verticales retournent à leur position initiale."""

#========================>Imporation de bibliothèques
import tkinter as tk 

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constante
couleur_fond_canvas = 'white'
couleur_fond_boutton = 'darkgreen'
zero = 0
deux_cents = 200
quatre_cents = 400
six_cents = 600

#========================>Fonction
def decalage(event):
    global ligne_left, ligne_right,zero, deux_cents, quatre_cents, six_cents
    if 0 < event.x < 200:
        canvas.coords(ligne_left, deux_cents-10, zero, deux_cents-10, six_cents)
        canvas.coords(ligne_right, quatre_cents-10, zero, quatre_cents-10, six_cents)
        
screen.bind('<Button-1>', decalage)


#========================>Programme principal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width = 600, height = 600, bg = couleur_fond_canvas)
boutton_restart = tk.Button(screen, text = 'Recommencer', bg = couleur_fond_boutton)

ligne_left = canvas.create_line((deux_cents, zero), (deux_cents, six_cents), fill = 'black', width = 2)
ligne_right = canvas.create_line((quatre_cents, zero), (quatre_cents, six_cents), fill = 'black', width = 2)

canvas.create_rectangle((0,0), (199, 600), fill = 'red')
canvas.create_rectangle((401, 0), (600, 600), fill = 'blue')
#========================>Placement widgets
canvas.grid(column = 0, row = 0, columnspan = 3)
boutton_restart.grid(column = 1, row = 1)

#========================>Fin boucle
screen.mainloop()
