"""import random
import tkinter as tk

def affichage():
    """ """"Affi  che le nom du joueur qui doit jouer à son tour.""" """
    global tour_joueur
    if tour_joueur == 0:
        tour_joueur += 1 # Création de l'enchainement entre joueur 1 et joueur 2
    return label3.config(text="C'est au tour de " + liste_joueurs[tour_joueur]+ " de jouer")
    tour_joueur -= 1
    return label.config(text="C'est au tour de " + liste_joueurs[tour_joueur]+ " de jouer")
liste_joueurs = (nom_joueur1, nom_joueur2)

tour_joueur = random.randint(0,1)

racine = tk.Tk() # Création de la fenêtre racine
racine.title("JEU PUISSANCE 4") # ajoute un titre
label = tk.Label(racine, text="Prêt à vous affronter au Puissance 4 ?", font=("helvetica", "20")) # création du widget
label.grid(column=3, row=0) # positionnement du widget

nom_joueur1 = input("Quel est ton nom joueur 1 ?") # identification du joueur 1
nom_joueur2 = input("Quel est ton nom joueur 2 ?") # identification du joueur 2


label1 = tk.Label(racine, text="Joueur 2 = " + nom_joueur1, font=("helvetica", "10")) # création du joeur 1
label2 = tk.Label(racine, text="Joueur 2 = " + nom_joueur2, font=("helvetica", "10")) # création du joeur 2
label3 = tk.Label(racine, text=affichage(), font=("helvetica", "10"))
label1.grid(column=0, row=1) # positionnement du nom du joueur 1
label2.grid(column=0, row=2) # positionnement du nom du joeur 2



    









racine = tk.Tk() # Création de la fenêtre racine
racine.mainloop() # Lancement de la boucle principale"""

import random
import tkinter as tk

racine = tk.Tk()
HEIGHT = 600
WIDTH = 700
color = ["yellow","blue"]
cpt = 0
coord_blue = []
coord_yellow = []



nom_joueur1 = input("Quel est ton nom joueur 1 ?") # identification du joueur 1
nom_joueur2 = input("Quel est ton nom joueur 2 ?") # identification du joueur 2

def affichage():
    """"Affiche le nom du joueur qui doit jouer à son tour."""
    global tour_joueur
    if tour_joueur == 0:
        tour_joueur += 1 # Création de l'enchainement entre joueur 1 et joueur 2
    return label3.config(text="C'est au tour de " + liste_joueurs[tour_joueur]+ " de jouer")
    tour_joueur -= 1
    return label.config(text="C'est au tour de " + liste_joueurs[tour_joueur]+ " de jouer")
liste_joueurs = (nom_joueur1, nom_joueur2)

tour_joueur = random.randint(0,1)

list1 = [((0,0),(100,100)),((0,100),(100,200)),((0,200),(100,300)),
         ((0,300),(100,400)),((0,400),(100,500)),((0,500),(100,600))]

list2 = [((100,0),(200,100)),((100,100),(200,200)),((100,200),(200,300)),
         ((100,300),(200,400)),((100,400),(200,500)),((100,500),(200,600))]

#  Création des cercles
def jeton():
    global cpt

    cpt = 1 - cpt
    global list1
    canvas.create_oval(list1[-1],fill = color[cpt])
    if cpt == 0:
        coord_yellow.append(list1[-1])
    else:
        coord_blue.append(list1[-1])
    del list1[-1]





def jeton2():
    global cpt
    cpt = 1 - cpt
    global list2
    canvas.create_oval(list2[-1],fill = color[cpt])
    del list2[-1]


racine = tk.Tk() # Création de la fenêtre racine
racine.title("JEU PUISSANCE 4") # ajoute un titre
label = tk.Label(racine, text="Prêt à vous affronter au Puissance 4 ?", font=("helvetica", "20")) # création du widget
label.grid(column=3, row=0) # positionnement du widget

label1 = tk.Label(racine, text="Joueur 1 = " + nom_joueur1, font=("helvetica", "30")) # création du joeur 1
label2 = tk.Label(racine, text="Joueur 2 = " + nom_joueur2, font=("helvetica", "30")) # création du joeur 2
"""label3 = tk.Label(racine, text=affichage(), font=("helvetica", "10"))"""
label1.grid(column=0, row=1) # positionnement du nom du joueur 1
label2.grid(column=0, row=2) # positionnement du nom du joeur 2

button1 = tk.Button(racine,command=jeton)
button1.grid(row = 4, column = 0)
button2 = tk.Button(racine,command=jeton2)
button2.grid(row = 4, column = 1)
button3 = tk.Button(racine,command=jeton)
button3.grid(row = 4, column = 2)
button4 = tk.Button(racine,command=jeton)
button4.grid(row = 4, column = 3)
button5 = tk.Button(racine,command=jeton)
button5.grid(row = 4, column = 4)
button6 = tk.Button(racine,command=jeton)
button6.grid(row = 4, column = 5)
button7 = tk.Button(racine,command=jeton)
button7.grid(row = 4, column = 6)

canvas = tk.Canvas(racine, bg="red", height = HEIGHT, width = WIDTH)
canvas.grid(columnspan = 7,row = 5)

#  Création des lignes

for i in range(7):
    for j in range(8):
        canvas.create_rectangle((i * 100,j * 100),((i+1) *  100,(j+1) * 100),fill = "red")







racine.mainloop()