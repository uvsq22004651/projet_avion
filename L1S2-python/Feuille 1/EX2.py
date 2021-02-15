"""Exercice 2

    Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
    Attendre deux clics de l’utilisateur.
    Afficher une ligne bleue entre les deux points cliqués.
    Attendre de nouveau deux clics.
    Afficher une ligne rouge entre les deux nouveaux points cliqués.
    Au clic suivant, les deux lignes sont effacées et on recommence (c’est-à-dire on attend de nouveau 2 clics comme au point 2.)
    Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie pas la fenêtre graphique) et le nom du bouton devient “Restart”.
    Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”."""

#========================>Imporation de bibliothèques
import tkinter as tk

#========================>Initialisation
screen = tk.Tk()
screen.title('Fenêtre')

#========================>Constante
size = 500
couleur_fond_canvas = 'white'
couleur_fond_boutton = 'darkgreen'
nb_clic = 0
coordonnees = (0, 0)

#========================>Fonction
def tracer_ligne(event):
    global nb_clic, coordonnees 
    if nb_clic == 0:
        nb_clic += 1
        coordonnees = (event.x, event.y)
        print('point1', coordonnees)
    elif nb_clic == 1:
        global first_line
        nb_clic += 1
        first_line = canvas.create_line(coordonnees, (event.x, event.y), fill = 'blue')
        print('point2', event.x, event.y)
    elif nb_clic == 2:
        nb_clic += 1
        coordonnees = (event.x, event.y)
        print('point3', coordonnees)
    elif nb_clic == 3:
        global second_line
        nb_clic += 1    
        second_line = canvas.create_line(coordonnees, (event.x, event.y), fill = 'red')
        print('point4', event.x, event.y)
    elif nb_clic == 4:       
        nb_clic = 0
        canvas.delete(screen, first_line)
        canvas.delete(screen, second_line)
        print('SUPPR')
        
screen.bind('<Button-3>', tracer_ligne)

def pause():
    global nb_clic
    if boutton_pause['text'] == 'Pause':
        nb_clic += 5  
        boutton_pause['text'] = 'Restart'
    elif boutton_pause['text'] == 'Restart':
        boutton_pause['text'] = 'Pause'
        nb_clic -= 5
#========================>Programme principal
#========================>Initialisation widgets
canvas = tk.Canvas(screen, width = size, height = size, bg = couleur_fond_canvas)
boutton_pause = tk.Button(screen, text = 'Pause', bg = couleur_fond_boutton, command = pause)

#========================>Placement widgets
canvas.grid(column = 0, row = 0, columnspan = 3)
boutton_pause.grid(column = 1, row = 1)

#========================>Fin boucle
screen.mainloop()
