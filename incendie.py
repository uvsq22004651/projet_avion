################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_incendie
################################

################################# IMPORTATIONS DE LIBRAIRIES

# -*- coding: UTF-8 -*-

################################# IMPORTATIONS DE LIBRAIRIES

import tkinter as tk
from random import sample
import time

################################# CONSTANTES
#Taille Canvas 
SIZE = 500
COTE = 10
p=0.62
f = 0.3
n=50
unit=10

#Couleurs de parcelles

EAU = "blue"
FORET = "forest green"
PRAIRIE = "yellow"
FEU = "red"
CENDRES_TIEDES = "grey"
CENDRES_ETEINTES = "black"
DUREE_FEU = 0.015
DUREE_CENDRE = 0.015
################################# LISTES

COLORS = [EAU, FORET, PRAIRIE, FEU, CENDRES_TIEDES, CENDRES_ETEINTES]

################################# FONCTIONS

states=[[0]*n for _ in range(n)]


def fill_cell(states, line, col):
        A=(unit*col, unit*line)
        B=(unit*(col+1), unit*(line+1))
        state=states[line][col]
        color=COLORS[state]
        canvas.create_rectangle(A, B, fill=color, outline='')

def fill(states):
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)

def parcelles():
    """Création des parcelles d'eau, de forêt et de prairie"""
    global states
    units=[(line,col) for col in range(n) for line in range(n)]
    ntrees=int(n**2*f)
    nprairies=int(n**2*p)
    trees=sample(units,ntrees)
    prairies=sample(units,nprairies)
    states=[[0]*n for _ in range(n)]  
    for (i,j) in trees:
        states[i][j]=1
    for (i,j) in prairies:
        states[i][j]=2
    fill(states)
    return states
        
def voisins(n, i, j):
    """Survole toutes les parcelles pour éxaminer leur voisins"""
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
    if a in range(n) and b in range(n)]


def update_states(states):
    n=len(states)
    to_fire=[]
    for line in range(n):
        for col in range(n):
            if states[line][col]==3:
                time.sleep(DUREE_FEU)
                states[line][col]=4
                time.sleep(DUREE_CENDRE)
                states[line][col]=5
                for (i, j) in voisins(n, line, col):
                    if states[i][j]==2:
                        to_fire.append((i, j))
    for (line,col) in to_fire:
        states[line][col]=3
        #time.sleep(DUREE_FEU)

def propagate():
    global states
    update_states(states)
    canvas.delete("all")
    fill(states)
    canvas.after(150, propagate)

def fire(event):
    global states
    #print('\n'.join(' '.join(map(str, L)) for L in states))
    
    x = int(event.x/10)
    y= int(event.y/10)
    print (x, y)
    states[x][y] = 3
    fill(states)
    propagate()


    
################################# PROGRAMME PRINCIPALE 
racine = tk.Tk()
racine.title("Incendie")

################################
# Création des widgets

canvas = tk.Canvas(racine, width=SIZE, height=SIZE, bg="white", borderwidth=0, highlightthickness=0)
bouton_commencer = tk.Button(racine, text="Création des parcelles", command=parcelles)
bouton_sauvegarder = tk.Button(racine, text="Sauvegarder")
bouton_importer = tk.Button(racine, text='Importer')
bouton_pause = tk.Button(racine, text="Pause")

################################
# Placement des widegts

canvas.grid(column=0, row=1, columnspan=4)
bouton_commencer.grid(column=2, row=2)
bouton_sauvegarder.grid(column=2, row=0)
bouton_importer.grid(column=1, row=0)
bouton_pause.grid(column=1, row=2)
canvas.bind('<Button-1>', fire)

################################
# Fin de la boucle



racine.mainloop()
