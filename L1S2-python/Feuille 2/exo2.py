import tkinter as tk
import random as rd

# variables globales

nb_clic = 0



# fonctions

def start():
    """Gestion clic sur le bouton"""
    global nb_clic
    if nb_clic == 0:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    nb_clic = 1 - nb_clic

def creer_balle():
    """Dessine un cercle de rayon 20 et retourne une liste contenant les infos de déplacement du cercle"""
    cercle = canvas.create_oval((300-20, 200-20), (300+20, 200+20), fill="blue")
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    return [cercle, dx, dy]


def mouvement(balle):
    """Déplace la balle de balle[1] pixels en abscisse et balle[2] pixels en ordonnée"""
    global id_after
    canvas.move(balle[0], balle[1], balle[2])
    rebond1(balle)
    id_after = canvas.after(20, lambda: mouvement(balle))


def rebond1(balle):
    x1, y1, x2, y2 = canvas.coords(balle[0])
    if x2 >= 600 or x1 <=0:
        balle[1] = -balle[1]
    if y2 >= 400 or y1 <= 0:
        balle[2] = -balle[2]


# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, width=600, height=400, bg="black")
canvas.grid()
bouton = tk.Button(racine, text="Démarrer", command=start)
bouton.grid(row=1)
balle = creer_balle()



racine.mainloop()