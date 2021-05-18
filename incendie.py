################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Projet_avion
#Yannis KYRIASIS
#Nadir HADIOUI
#Ismael AYAD
#Oumou ATJI
#Nabil SABER
#https://github.com/uvsq22004651/projet_avion/edit/main/incendie.py
################################

################################ Fonctionnement du programme
"""Ce code est une simulation de passager ce plaçant à une place qui leur est 
attribué à bord d'un avion. Si deux passager sont l'un derrière l'autre, le premier 
dans le couloir de l'avion, le premier doit attendre que le second se soit placé à sont
siège. Chaque passager à 0,1 ou 2 bagages"""

################################# IMPORTATIONS DE LIBRAIRIES
import tkinter as tk
import random as rd

################################ INITIALISATION
screen = tk.Tk()
screen.title("Simulation avion")

################################# CONSTANTES
SIEGES_VIDES = "steel blue"
COULOIR = "light steel blue"
ZERO_BAGAGE = "yellow"
UN_BAGAGE = "orange"
DEUX_BAGAGES = "red"
SIEGES_OCCUPEES = "green"
LARGEUR = 140
HAUTEUR = 600

#Longeur des carrés qui constituent le quadrillage
COTE = 20
NB_COl = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

################################# VARIABLES
#Initialisations des listes et des variables
tableau = None
coordonnées = None
liste_passagers = None
voisins_milieu = 0
voisins_gauche = 0
voisisns_droite = 0

################################# FONCTIONS
def sieges_couloir():
    global COTE, SIEGES, COULOIR
    """Création des sièges de l'avion et du couloir de l'avion"""
    for i in range (7): #Création des colonnes
        for j in range (30): #Création des lignes
                celule = canvas.create_rectangle(i*COTE, j*COTE, (1+i)*COTE, (1+j)*COTE, fill = SIEGES)
                if i == 3:
                    canvas.itemconfig(celule, fill = COULOIR)


def coordonnees_sieges():
    """Attribue une coordonnée à chaques sièges de l'avion sous forme
    de tableau à deux dimensions"""
    coordonnées = []
    for col in range (1,4):
        for line in range (1,31):
            coordonnées.append([col, line]) #Sièges à gauche du couloir
    for col in range (4, 8):
        for line in range (1, 31):
            coordonnées.append([col, line]) #Sièges à droite du couloir
    return coordonnées


def tableau_2D():
    """Création d'un tableau à deux dimension permettant de connaître
    le rôle de chaque celule, le couloir est initilisé à 0, tandis 
    que les sièges sont initialisés à 1"""
    global tableau
    tableau = []
    for i in range(NB_COl):
        if i == 3:
            tableau.append([0]*NB_LINE) #Couloir
        else:
            tableau.append([1]*NB_LINE) #Sièges
    return tableau


def création_passagers_bagages():
    """Création des 180 passagers numéroté de 0 à 179 à qui on affecte un
    chiffre entre 0 et 2 qui correspond au nombre de bagage(s)"""
    global coordonnées
    liste_passagers = []
    for passagers in range (180): 
        liste_passagers.append([passagers]) #Donne un numéro à chaque passager
        for bagages in range (1):
            liste_passagers[passagers].append(rd.randint(0,2)) #Donne entre 0 et 2 bagages aléatoirement
    return liste_passagers 

class passeegr: 
        def __init__(self,num,x,y,bagages=[]):
    self.x,self.y=x,y
    self.bagages=bagages
class Cellule:
  
  def __init__(self,x,y,typeC):
    if typeC in ['couloir','siege']:
      self.typeC=typeC
      self.x,self.y=x,y
    else :
      raise ValueError("type non reconnu")
    
    self.passenger=None
 
  def __str__(self):
    i,j=self.x,self.y
    if i==4:
         return "couloir"
    if i < 10:
          i="0"+str(i)
    if j < 10:
          j="0"+str(j)  

          if passenger = 0 : 
              print(passager is yellow ) 
                
else : 
    if passagers = 1 : 
        print(passager is orange )

else : 
    if passager = 2 : 
        print(passagers is red)
   return str(i)+" "+str(j)

def coordonnées_passagers():
    """Donne une place à chaque passager de manière aléatoire"""
    global liste_passagers, coordonnées
    for i in range(180):
        place = rd.randint(180) #Choisi un nombre au hasard
        liste_passagers[i].append(coordonnées[place]) #Ajoute la place dans la liste liste_passagers
        coordonnées.remove[place] #Supprime la place de la liste coordonnées
    return liste_passagers


def voisins_couloir():
    """Examine le couloir de l'avion pour savoir si les passagers ont
    des voisins devant eux"""
    global tableau
    voisins_milieu = 0
    for v in range(3, 4):
        for w in range(NB_LINE):
            if tableau[v][w] != 0 and [v, w] != [i, j]:
                voisins_milieu += 1
    return voisins_milieu


def voisins_sièges_gauche():
    """Examine les sièges à gauche du couloir pour voir si un passager
    est déjà placé"""
    global tableau
    voisins_gauche = 0
    for v in range(0, 3):
        for w in range(NB_LINE):
            if tableau[v][w] != 0 and [v, w] != [i, j]:
                voisins_gauche += 1
    return voisins_gauche
                    

def voisins_sièges_droite():
    global tableau
    """Examine les sièges à droite du couloir pour voir si un passager
    est déjà placé"""
    voisins_droite = 0
    for v in range(4, 7):
        for w in range(NB_LINE):
            if tableau[v][w] != 0 and [v, w] != [i, j]:
                voisins_droite += 1
    return voisins_droite
    

def legende():
    """Création d'une légende pour définir chaques carrés de couleur"""
    canvas.create_rectangle((180, 40), (200, 60), fill = SIEGES_VIDES)
    leg_siege = tk.Label(screen, text = "Siège", font = "Arial")
    leg_siege.grid(column = 1, row = 0) 

    canvas.create_rectangle((180, 140), (200, 160), fill = COULOIR)
    leg_couloir = tk.Label(screen, text = "Couloir", font = "Arial")
    leg_couloir.grid(column =1, row = 1)

    canvas.create_rectangle((180, 240), (200, 260), fill = ZERO_BAGAGE)
    leg_zero_bagage = tk.Label(screen, text = "Passager avec aucun bagage", font = "Arial")
    leg_zero_bagage.grid(column = 1, row = 2)

    canvas.create_rectangle((180, 340), (200, 360), fill = UN_BAGAGE)
    leg_un_bagage = tk.Label(screen, text = "Passager avec un bagage", font = "Arial")
    leg_un_bagage.grid(column = 1, row = 3)

    canvas.create_rectangle((180, 440), (200, 460), fill = DEUX_BAGAGES)
    leg_deux_bagage = tk.Label(screen, text = "Passager avec deux bagages", font = "Arial")
    leg_deux_bagage.grid(column = 1, row =4)

    canvas.create_rectangle((180, 540), (200, 560), fill = SIEGES_OCCUPEES)
    leg_place = tk.Label(screen, text = "Passager assis à sa place", font = "Arial")
    leg_place.grid(column = 1, row = 5)


################################# PROGRAMME PRINCIPALE 
canvas = tk.Canvas(screen, width = 280, height = 600, borderwidth=0, highlightthickness=0, bg = "black")
sieges_couloir()
legende()

################################# PLACEMENT DES WIDGETS
canvas.grid(column = 0, row = 0, rowspan = 6)

################################# FIN DE LA BOUCLE
screen.mainloop()
