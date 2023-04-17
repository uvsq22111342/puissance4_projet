

import tkinter as tk
import random as random
import math as math


colonne = int(input("Choisir un nombre de colonnes"))
ligne = int(input("Choisir un nombre de lignes"))
puissance = int(input("Choisir le nombre de jetons à aligner pour gagner"))
manche = int(input("Combien de manches faut-il gagner ?"))
joueur = [0,0]
color = ["lemonchiffon","plum"]


HEIGHT = 700
WIDTH = 700

hauteur = math.floor(HEIGHT / ligne)
largeur = math.floor(WIDTH / colonne)


def sauvegarder(event):
    " Sauvegarde la partie dans un fichier texte"
    global cpt, coord_red_tot,coord_yellow_tot, colonne, ligne, puissance, manche, joueur
    f_input=open("puissance4.txt",'w')
    f_input.write(str(colonne) + "\n")
    f_input.write(str(ligne) + "\n")
    f_input.write(str(coord_red_tot) + "\n")
    f_input.write(str(coord_yellow_tot) + "\n")
    f_input.write(str(puissance) + "\n")
    f_input.write(str(manche) + "\n")
    f_input.write(str(joueur[0]) + "\n")
    f_input.write(str(joueur[1]) + "\n")
    f_input.write(str(cpt) + "\n")
    f_input.close()


def charger(event):
    " Charge la partie du fichier texte "
    global cpt, coord_red_tot,coord_yellow_tot, coord,coord_red_abs,coord_red_ord,coord_yellow_abs,coord_yellow_ord, colonne, ligne, puissance, manche, joueur, largeur, hauteur
    reboot()
    f_output = open("puissance4.txt",'r')
    colonne = int(f_output.readline())
    ligne = int(f_output.readline())
    hauteur = math.floor(HEIGHT / ligne)
    largeur = math.floor(WIDTH / colonne)
    coord_red_tot = trad(list(f_output.readline()))
    coord_yellow_tot = trad(list(f_output.readline()))
    puissance = int(f_output.readline())
    manche = int(f_output.readline())
    joueur1 = int(f_output.readline())
    joueur2 = int(f_output.readline())
    joueur = [joueur1, joueur2]
    cpt = int(f_output.readline())
    f_output.close()
    coord = [[(i*largeur,j*hauteur) for j in range(1,ligne +1)] for i in range(1,colonne+1)]
    for i in range(colonne):
        for j in range(ligne):
            canvas.create_rectangle((i * largeur,j * hauteur),((i+1) *  largeur,(j+1) * hauteur),fill = "royalblue")
    for i in coord_red_tot:
        canvas.create_oval((i[0]-largeur,i[1]-hauteur),i, fill = "plum")
        for j in coord:
            if i in j:
                j.remove(i)
    for i in coord_yellow_tot:
        canvas.create_oval((i[0]-largeur,i[1]-hauteur),i, fill = "lemonchiffon")
        for j in coord:
            if i in j:
                j.remove(i)
    coord_red_abs = [i[0] for i in coord_red_tot]
    coord_red_ord = [i[1] for i in coord_red_tot]
    coord_yellow_abs = [i[0] for i in coord_yellow_tot]
    coord_yellow_ord = [i[1] for i in coord_yellow_tot]
    update()
    


def trad(list):
    " Transforme la liste du fichier texte en liste utilisable par le code "
    l = []
    z = [ '[', '(',',',']',')','\n',' ']
    l = [int(k) for k in list if k not in z]
    l.append(1)
    L = []
    if len(l)%3 == 1:
        l.pop()
    for i in range(0,len(l),3):
        j = int(str(l[i])+str(l[i+1])+str(l[i+2]))
        L.append(j)
    W = [(L[i],L[i+1]) for i in range(0,len(L)-1,2)]
    return W


racine = tk.Tk()
racine.title("JEU PUISSANCE 4")

canvas = tk.Canvas(racine, bg="royalblue", height = HEIGHT, width = WIDTH)
label = tk.Label(racine, text="Nombre de manches à gagner : "+str(manche), font=("helvetica", "20")) 
label2 = tk.Label(racine, text="joueur 1 a gagné " + str(joueur[0]) + " manche ", font=("helvetica", "20"),bg = color[0])
label3 = tk.Label(racine, text="joueur 2 a gagné " + str(joueur[1]) + " manche ", font=("helvetica", "20"),bg = color[1])


canvas.grid(row = 0, column = 0, rowspan = ligne, columnspan = colonne)
label.grid(row = 0, column = colonne)
label2.grid(row = 1, column = colonne)
label3.grid(row = 2, column = colonne)

cpt = random.randint(0,1)
coord = [[(i*largeur,j*hauteur) for j in range(1,ligne +1)] for i in range(1,colonne+1)]
coord_yellow_abs = []
coord_yellow_ord = []
coord_red_abs = []
coord_red_ord = []
coord_red_tot = []
coord_yellow_tot = []

# Création des lignes


for i in range(colonne):
    for j in range(ligne):
        canvas.create_rectangle((i * largeur,j * hauteur),((i+1) *  largeur,(j+1) * hauteur),fill = "royalblue")


# Placement des jetons


def jeton(event):
    " Place les jetons en fonction de la couleurs et des cases disponibles "
    global cpt, coord, coord_red_abs,coord_red_ord,coord_yellow_abs,coord_yellow_ord, coord_red_tot,coord_yellow_tot, joueur
    colox = math.floor(event.x / largeur)
    if colox <= colonne:
        canvas.create_oval((coord[colox][-1][0]-largeur,coord[colox][-1][1]-hauteur),coord[colox][-1], fill = color[cpt])
        if cpt == 0:
            coord_yellow_abs.append(coord[colox][-1][0])
            coord_yellow_ord.append(coord[colox][-1][1])
            coord_yellow_tot.append(coord[colox][-1])
        else:
            coord_red_abs.append(coord[colox][-1][0])
            coord_red_ord.append(coord[colox][-1][1])
            coord_red_tot.append(coord[colox][-1])
        del coord[colox][-1]
        if win_try(coord_yellow_abs,coord_yellow_ord) or win_try(coord_yellow_ord,coord_yellow_abs) or \
            win_try(coord_red_abs,coord_red_ord) or win_try(coord_red_ord,coord_red_abs) or \
            diag(coord_red_tot) or diag(coord_yellow_tot) or diag2(coord_red_tot) or diag2(coord_yellow_tot):
            joueur[cpt] += 1
            update()
            if joueur[cpt] == manche:
                label["text"] = "Le joueur "+str(cpt + 1) + " a gagné !"
            else:
                reboot()
        if nulle(coord):
            reboot()
        cpt = 1 - cpt


# Conditions de victoire:


def win_try(list1,list2):
    " Vérifie s'il y a puissances jetons de la meme couleur alignés verticalement ou horizontalement "
    global puissance
    L = []
    if len(list1) > puissance - 1:
        for i in range(len(list1)):
            var1_i = list1.count(list1[i])
            if var1_i > puissance - 1:
                indices_var1_i = [j for j in range(len(list1)) if list1[j]==list1[i]]
                var2 = [list2[l] for l in indices_var1_i]
                var2.sort()
                for k in range(0,len(var2)-puissance+1):
                    S = 0
                    for i in range(k,k+puissance):
                        S += var2[i]
                    if S == var2[k]*puissance +(puissance)*(puissance-1)//2 * largeur:
                        return True
                    elif S == var2[k]*puissance +(puissance)*(puissance-1)//2 * hauteur:
                        return True


def diag(list):
    " Verifie s'il y a puissances jetons de la meme couleur alignés diagonalement droite bas ou haut gauche "
    global puissance
    for (abs,ord) in list:
        S = 0
        for i in range(puissance):
            if (abs+largeur,ord+hauteur) in list:
                S += 1
                abs += largeur
                ord += hauteur
        if S == puissance - 1:
            return True


def diag2(list):
    " Verifie s'il y a puissances jetons de la meme couleur alignés diagonalement haut droite ou bas gauche "
    global puissance
    for (abs,ord) in list:
        S = 0
        for i in range(puissance):
            if (abs-largeur,ord+hauteur) in list:
                S += 1
                abs -= largeur
                ord += hauteur
        if S == puissance - 1:
            return True

def nulle(coord):
    S = 0
    for i in coord:
        if i != []:
            S += 1
    if S == 0:
        return True


def retour(event):
    " Supprime le dernier jeton joué "
    global cpt, coord_red_abs, coord_yellow_abs, coord_red_ord, coord_yellow_ord, coord_red_tot, coord_yellow_tot
    try:
        if cpt == 0:
            couple = coord_red_tot[-1]
            del coord_red_tot[-1]
            del coord_red_ord[-1]
            del coord_red_abs[-1]
        else:
            couple = coord_yellow_tot[-1]
            del coord_yellow_tot[-1]
            del coord_yellow_ord[-1]
            del coord_yellow_abs[-1]
        for i in range(colonne+1):
            if couple[0] == largeur*(i+1):
                coord[i].append(couple)
                jeton = canvas.find_closest(couple[0]-largeur//2,couple[1]-hauteur//2)
        canvas.delete(jeton)
        cpt = 1 - cpt
    except:
        pass


def reboot():
    " Redémarre la partie "
    global cpt, coord, coord_red_abs,coord_red_ord,coord_yellow_abs,coord_yellow_ord, coord_red_tot,coord_yellow_tot, largeur, hauteur
    coord = [[(i*largeur,j*hauteur) for j in range(1,ligne +1)] for i in range(1,colonne+1)]
    coord_yellow_abs = []
    coord_yellow_ord = []
    coord_red_abs = []
    coord_red_ord = []
    while len(coord_yellow_tot) != 0:
        jeton2 = canvas.find_closest(coord_yellow_tot[-1][0]-largeur // 2,coord_yellow_tot[-1][1]-hauteur//2)
        canvas.delete(jeton2)
        del coord_yellow_tot[-1]
    while len(coord_red_tot) != 0:
        jeton = canvas.find_closest(coord_red_tot[-1][0]-largeur // 2,coord_red_tot[-1][1]-hauteur// 2)
        canvas.delete(jeton)
        del coord_red_tot[-1]


def update():
    " Rafraichis en fonction du nombre de manches gagnés "
    if joueur[0] > 1:
        label2["text"] = "joueur 1 a gagné " + str(joueur[0]) + " manches"
    else:
        label2["text"] = "joueur 1 a gagné " + str(joueur[0]) + " manche"
    if joueur[1] > 1:
        label3["text"] = "joueur 2 a gagné " + str(joueur[1]) + " manches"
    else:
        label3["text"] = "joueur 2 a gagné " + str(joueur[1]) + " manche"
    label["text"] = "Nombre de manches à gagner : "+str(manche)




racine.bind('<Button-1>',jeton)
racine.bind('<BackSpace>',retour)
racine.bind('s',sauvegarder)
racine.bind('c',charger)



racine.mainloop()