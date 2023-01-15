# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:13:25 2022

@author: Loïc & Rémi
"""
import turtle as t
from random import randint
import time


### variables globales                                                                                                            ###
# dictionnaire des touches                                                                                                          #
controles = {"up":"Up",                                                                                                             #
            "down":"Down",                                                                                                          #
            "left":"Left",                                                                                                          #
            "right":"Right",                                                                                                        #
            "enter":"Return",                                                                                                       #
            "fullscreen":"F11",                                                                                                     #
            "echap":"Escape"}                                                                                                       #
font = "Bungee"                                                                                                                     # police d'écriture global, installer la police Bungee sur votre ordinateur
taille_fenetre = (1440, 720)                                                                                                        # taille de la fenêtre par défaut
## variables des personnages                                                                                                       ##
couleurs = [[0,(203,79,15),(5,5,5),(255,191,179)],                                                                                  # 0, goomba
            [0,(221,31,38),(130,66,32),(239,189,139),(0,0,0),(77,89,167),(253,232,33)],                                             # 1, mario
            [0,(232,53,43),(135,4,4),(236,243,163),(5,155,9),(255,255,255),(255,192,0),(67,64,75),(177,119,40)],                    # 2, bowser
            [0,(254,224,196),(225,84,13),(4,3,8)],                                                                                  # 3, block
            [0,(255,255,255),(5,5,5),(255,191,179)],                                                                                # 4, goomba (mort)
            [0,(31,35,36),(255,255,255),(189,190,222),(214,217,243)],                                                               # 5, flèche
            [0,(255,255,255)]]                                                                                                      # 6, logo bowser (game over)
personnages = [[[0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],                                                                              # 0, goomba
                [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],                                                                              #
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],                                                                              #
                [0,0,0,1,2,2,1,1,1,1,1,1,2,2,1,0,0,0],                                                                              #
                [0,0,1,1,1,3,2,1,1,1,1,2,3,1,1,1,0,0],                                                                              #
                [0,0,1,1,1,3,2,2,2,2,2,2,3,1,1,1,0,0],                                                                              #
                [0,1,1,1,1,3,2,3,1,1,3,2,3,1,1,1,1,0],                                                                              #
                [0,1,1,1,1,3,3,3,1,1,3,3,3,1,1,1,1,0],                                                                              #
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],                                                                              #
                [0,0,1,1,1,1,3,3,3,3,3,3,1,1,1,1,0,0],                                                                              #
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],                                                                              #
                [0,0,0,0,2,2,3,3,3,3,3,3,2,2,0,0,0,0],                                                                              #
                [0,0,0,0,2,2,2,3,3,3,3,2,2,2,0,0,0,0],                                                                              #
                [0,0,0,0,0,2,2,2,0,0,2,2,2,0,0,0,0,0]],                                                                             #
               [[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],                                                                              # 1, mario
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,2,2,2,3,3,4,3,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,2,3,2,3,3,3,4,3,3,3,0,0,0,0],                                                                              #
                [0,0,0,0,2,3,2,2,3,3,3,4,3,3,3,0,0,0],                                                                              #
                [0,0,0,0,2,2,3,3,3,3,4,4,4,4,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,1,1,5,1,1,1,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,1,1,1,5,1,1,5,1,1,1,0,0,0,0],                                                                              #
                [0,0,0,1,1,1,1,5,5,5,5,1,1,1,1,0,0,0],                                                                              #
                [0,0,0,3,3,1,5,6,5,5,6,5,1,3,3,0,0,0],                                                                              #
                [0,0,0,3,3,3,5,5,5,5,5,5,3,3,3,0,0,0],                                                                              #
                [0,0,0,3,3,5,5,5,5,5,5,5,5,3,3,0,0,0],                                                                              #
                [0,0,0,0,0,5,5,5,0,0,5,5,5,0,0,0,0,0],                                                                              #
                [0,0,0,0,2,2,2,0,0,0,0,2,2,2,0,0,0,0],                                                                              #
                [0,0,0,2,2,2,2,0,0,0,0,2,2,2,2,0,0,0]],                                                                             #
               [[0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0],                                                                              # 2, bowser
                [0,0,0,0,0,0,0,1,2,2,1,2,1,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,3,0,0,1,3,2,1,2,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,3,3,4,1,3,1,1,4,4,1,0,0,0],                                                                              #
                [0,0,0,0,0,1,1,4,4,3,3,1,1,1,4,0,0,0],                                                                              #
                [0,0,0,3,4,4,5,5,4,4,4,4,5,2,1,3,3,0],                                                                              #
                [0,0,0,3,3,5,6,7,4,3,3,4,4,4,3,3,7,3],                                                                              #
                [0,0,0,1,7,6,6,7,4,3,1,3,3,3,3,3,3,3],                                                                              #
                [0,0,0,6,7,7,6,7,7,3,3,1,5,1,5,1,5,0],                                                                              #
                [0,0,7,6,6,7,7,8,7,7,3,3,3,3,3,3,0,0],                                                                              #
                [0,6,7,7,6,6,8,8,8,7,7,7,7,7,7,6,7,0],                                                                              #
                [0,6,6,7,7,8,8,6,3,3,3,3,3,3,6,7,7,0],                                                                              #
                [0,5,6,6,6,5,6,6,3,3,3,3,3,3,7,7,6,6],                                                                              #
                [6,0,5,6,5,8,8,8,6,6,6,6,6,6,8,6,6,5],                                                                              #
                [6,6,6,8,8,6,6,6,8,3,3,3,3,3,8,6,5,0],                                                                              #
                [0,6,6,8,6,6,6,6,8,6,6,6,6,8,6,6,0,0],                                                                              #
                [0,0,6,8,6,6,6,6,8,8,3,3,8,3,3,3,0,0],                                                                              #
                [0,0,0,0,6,5,6,5,6,0,0,0,6,6,6,5,6,5]],                                                                             #
               [[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],                                                                              # 3, block
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],                                                                              #
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],                                                                              #
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],                                                                              #
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],                                                                              #
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],                                                                              #
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],                                                                              #
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],                                                                              #
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],                                                                              #
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],                                                                              #
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],                                                                              #
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0]],                                                                             #
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              # 4, goomba mort
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,2,2,0,0,2,2,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,2,1,1,2,2,1,1,2,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,2,1,1,1,1,1,1,2,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],                                                                              #
                [0,0,0,0,2,2,3,3,3,3,3,3,2,2,0,0,0,0],                                                                              #
                [0,0,0,0,2,2,2,3,3,3,3,2,2,2,0,0,0,0],                                                                              #
                [0,0,0,0,0,2,2,2,0,0,2,2,2,0,0,0,0,0]],                                                                             #
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              # 5, flèche
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],                                                                              #
                [0,1,1,1,1,1,1,1,1,1,1,4,4,1,0,0,0,0],                                                                              #
                [1,2,2,2,2,2,2,2,2,2,2,2,2,4,1,0,0,0],                                                                              #
                [1,2,2,2,2,2,2,2,2,2,4,2,2,2,4,1,0,0],                                                                              #
                [1,2,3,4,4,4,4,4,4,4,4,4,2,2,2,4,1,0],                                                                              #
                [1,2,3,4,4,4,4,4,4,4,4,4,4,2,2,2,4,1],                                                                              #
                [1,2,3,4,4,4,4,4,4,4,4,4,2,2,2,4,1,0],                                                                              #
                [1,2,2,2,2,2,2,2,2,2,4,2,2,2,4,1,0,0],                                                                              #
                [1,2,2,2,2,2,2,2,2,2,2,2,2,4,1,0,0,0],                                                                              #
                [0,1,1,1,1,1,1,1,1,1,1,4,4,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0]],                                                                             #
               [[0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],                                                                              # 6, logo bowser (pour ecran de game over)
                [0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0],                                                                              #
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0],                                                                              #
                [0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0],                                                                              #
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],                                                                              #
                [0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0],                                                                              #
                [0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0],                                                                              #
                [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0],                                                                              #
                [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0]]]                                                                             #
## FIN variables personnages                                                                                                       ##
### FIN variables globales                                                                                                        ###


def debug_personnages(turtle=t) -> None:
    """Affiche les personnages pour les tests."""
    turtle.tracer(0)                                                                                                                # désactive l'animation de la tortue (pour gagner en vitesse)
    turtle.colormode(255)                                                                                                           # mode couleur rgb
    turtle.hideturtle()                                                                                                             # cache la tortue
    turtle.up()                                                                                                                     # lève le crayon
    turtle.goto(-200,300)                                                                                                           # positionne la tortue
    turtle.down()                                                                                                                   # baisse le crayon
    for i in range(len(personnages)):                                                                                               # pour chaque personnage:
        print_personnage(8,i)                                                                                                       # affiche le personnage d'indice i à la taille 8
    turtle.exitonclick()                                                                                                            # attend un clic de la souris pour quitter


def setenv() -> None:
    """Initialise la fenêtre de jeu."""
    global taille_fenetre,cv
    wm=t.Screen()                                                                                                                   # recupere la fenetre
    wm.bgcolor("black")                                                                                                             # définie le noir comme couleur d'arrière plan
    wm._root.iconbitmap(r'star.ico')                                                                                                # icône de la fenêtre
    wm.setup(taille_fenetre[0],taille_fenetre[1])                                                                                   # définie la taille de la fenetre
    wm._root.resizable(False, False)                                                                                                # empêche le redimensionnement de la fenêtre
    cv=wm.getcanvas()                                                                                                               # récupère la fenêtre de jeu
    cv.winfo_toplevel().attributes("-fullscreen", False)                                                                            # met la fenêtre en mode fenêtré
    cv.config(highlightthickness=0,selectborderwidth=0,insertwidth=0,bd=0,closeenough=0,confine=0)                                  # supprime la bordure de plein écran
    wm.title("SUPER MARIO ALLUMETTES.")                                                                                             # titre de la fenêtre
    wm.tracer(0)                                                                                                                    # désactive l'animation de la tortue (pour gagner en vitesse)
    wm.colormode(255)                                                                                                               # mode couleur rgb
    wm.bgpic("bgrd.gif")                                                                                                            # image de fond
    t.hideturtle()                                                                                                                  # cache la tortue


def toggle_fullscreen() -> None:
    """Active/Désactive le mode plein écran."""
    global cv
    cv.winfo_toplevel().attributes("-fullscreen",not(cv.winfo_toplevel().attributes("-fullscreen")))                                # inverse l'état du mode plein écran


def text(texte:str, x:int, y:int, couleur="white",align="center", taille:int=20 ,style="normal", offset=(1,3), t=t) -> None:
    """Affiche un texte à l'écran, avec une effet de profondeur, dû au décalage."""
    global font                                                                                                                     # variable globale de la police d'écriture
    if type(offset) == int:                                                                                                         # si le décalage est un entier applique aux 2 coordonnées
        offset = (offset, offset)                                                                                                   # crée un décalage 
    t.up()                                                                                                                          # lêve le stylo
    t.goto(x+offset[0], y-offset[1])                                                                                                # téléporte la tortue en fonction du décalage
    t.down()                                                                                                                        # pose le stylo
    t.color("black")                                                                                                                # le stylo écrit en noir 
    t.write(texte, align=align, font=(font, taille, style))                                                                         # écrit les différents titres de l a page d'accueil
    t.up()                                                                                                                          # lève le stylo
    t.goto(x, y)                                                                                                                    # téléporte la tortue en x,y 
    t.down()                                                                                                                        # pose le stylo
    t.color(couleur)                                                                                                                # set la couleur avec la valeur de la variable couleur 
    t.write(texte, align=align, font=(font, taille, style))                                                                         # écrit les titres(en blanc)
    t.up()                                                                                                                          # lève le stylo


def print_personnage(s:int,personnage:int,t=t):
    global personnages, couleurs                                                                                                    # appelle les variables stockées dans varaibles personnages,couleurs
    t.width(0)                                                                                                                      # set l'épaisseur du stylo  0
    for ligne in personnages[personnage]:                                                                                           # crée la boucle pour le tracer les personnages
        for couleur in ligne:                                                                                                       # pour les couleurs dans la ligne
            if couleur!=0:                                                                                                          # si la couleur est différente de 0
                t.down()                                                                                                            # pose le stylo 
                t.color(couleurs[personnage][couleur])                                                                              # set la couleur du stylo, en fonction des couleurs contenues dans couleur
                t.fillcolor(couleurs[personnage][couleur])                                                                          # set la couleur de remplissage, en fonction des couleurs contenues dans couleur
                t.begin_fill()                                                                                                      # commence le remplissage de couleur
                for _ in range(4):                                                                                                  # pour les 4 côtés du carré
                    t.forward(s)                                                                                                    # la tortue avance de s 
                    t.right(90)                                                                                                     # la tortue tourne de 90 degrés 
                t.end_fill()                                                                                                        # arrête le remplissage de couleur 
            t.up()                                                                                                                  # lève le stylo
            t.forward(s+1)                                                                                                          # avance de s+1 pour tracer un autre personnage 
        t.backward((s+1)*18)                                                                                                        # retourne en arrière pour revenir point départ de la ligne 
        t.right(90)                                                                                                                 # oriente la tortue vers le bas (pour changer de tas)
        t.forward(s+1)                                                                                                              # descendre de s+1 pour créer nouveau tas en desspus 
        t.left(90)                                                                                                                  # oriente à gauche pour générer nouveaux personnagex 


def hide_title(t=t):
    """Cache le titre du jeu."""                                                                                                    
    t.color(160,172,254)                                                                                                            # set la couleur au bleu 
    t.goto(-225,0)                                                                                                                  # se téléporte aux coordonnées du rectangle du titre 
    t.down()                                                                                                                        # pose le stylo
    t.begin_fill()                                                                                                                  # commence le remplissage 
    for _ in range(4):                                                                                                              # pour les 4 côtés du rectangle
        t.forward(450 - 228 * (_ % 2))                                                                                              # avance de la longueur du titre
        t.left(90)                                                                                                                  # tourne de 90 degrés
    t.end_fill()                                                                                                                    # fin du renmplissage 


def set_goomba(j: int, i: int, alive: int, turtle=t):
    """Affiche le personnage de coordonnées (j,i) sur la fenêtre.
    j est le numéro du tas, i est le numéro du personnage dans le tas.
    perso est le numéro du personnage à afficher."""
    global taille_fenetre
    turtle.up()                                                                                                                     # lève la tortue 
    turtle.clear()                                                                                                                  # efface le goomba (mort ou vivant)
    turtle.goto(taille_fenetre[0]//2-114-119*i-1, -taille_fenetre[1]//2+183+140*j)                                                  # trace le premier goomba aux coordonnées définies
    print_personnage(3,0 if alive else 4,turtle)                                                                                    # affiche goomba vivant si vivant, goomba mort si mort 


def setpersonnages(l_tas: list[int], list_turtle=[]):
    """Affiche les personnages (brick et goomba) sur la fenêtre."""       
    global taille_fenetre
    if list_turtle==[]:                                                                                                             # si la liste des tortues est vide
        list_turtle=[[t.Turtle() for _ in range(l_tas[k])] for k in range(len(l_tas))]                                              # crée la liste des tortues
    t.up()                                                                                                                          # leve le crayon
    t.hideturtle()                                                                                                                  # cache la tortue
    [i.up() for j in list_turtle for i in j]                                                                                        # lève le crayon pour toutes les tortue dans la liste de tortues
    [i.hideturtle() for j in list_turtle for i in j]                                                                                # cache toutes les tortues dans la liste de tortues
    coord=(taille_fenetre[0]-114, -taille_fenetre[1]+184)                                                                           # définit les coordonnées globales des goombas
    for j in range(len(l_tas)):                                                                                                     # pour chaque tas
        for i in range(l_tas[j]*2-1):                                                                                               # pour chaque goombas dans le tas (1 goombas toutes les 2 brick)
            if j!=0:                                                                                                                # si le tas n'est pas le premier
                t.goto(coord[0]-60*i-8-taille_fenetre[0]//2,coord[1]+140*j-65+taille_fenetre[1]//2)                                 # se téléporte aux coordonnées de la brick
                print_personnage(4, 3,t)                                                                                            # affiche la brick
            if i%2==0:                                                                                                              # si l'indice est pair
                set_goomba(j, i//2, 1, list_turtle[j][i//2])                                                                        # affiche un goomba
    return list_turtle                                                                                                              # retourne la liste des tortues


def setpersonnages_joueur(turtle=t, joueur=(1,1)):
    """Affiche mario et bowser."""
    global taille_fenetre                                                                                                           # appelle la variable stockée dans taille fenetre 
    coord=(40-taille_fenetre[0]//2,-taille_fenetre[1]//2+199)                                                                       # crée la variable des coordonnées des marios et bowsers 
    if joueur[1]:                                                                                                                   # si on veut afficher mario 
        turtle.goto(coord[0],coord[1])                                                                                              # place la tortue aux coordonnées voulues 
        print_personnage(4, 1,turtle)                                                                                               # affiche mario
    if joueur[0]:                                                                                                                   # si on veut afficher bowser 
        turtle.goto(coord[0]+160,coord[1]+10)                                                                                       # place la tortue aux coordonnées voulues 
        print_personnage(4, 2,turtle)                                                                                               # affiche bowser 


def set_fleche_joueur(joueur: int,turtle=t):
    """Affiche la flèche du joueur."""
    global taille_fenetre                                                                          
    coord= (128 if joueur else 295, -taille_fenetre[1]//2+300)                                                                      # appelle la variable stockée dans taille fenêtre 
    turtle.clear()                                                                                                                  # enlève travail de la flèche située sur un 
    turtle.up()                                                                                                                     # lève le stylo
    turtle.goto(coord[0]-taille_fenetre[0]//2,coord[1])                                                                             # place la tortue sur les coordonnées de la flèche de l'autre joueur 
    turtle.setheading(-90)                                                                                                          # flèche de base à l'horizontale permet de l'orienter verticale 
    print_personnage(3, 5,turtle)                                                                                                   # print la flèche sur le joueur 


def set_fleche_goomba(tas: int,direction: int,turtle=t):
    """Affiche la flèche coulissant entre les tas de goombas."""
    global taille_fenetre, nb_tas_global                                                                                            # appelle variable stockée dans taille_fenêtre 
    coord=(taille_fenetre[0]//2-1066, -taille_fenetre[1]//2+200)                                                                    # définie coordonnées pour fleche goomba
    r = [tas-0.5*direction,tas] if direction else [tas]                                                                             # définit les tas sur lesquels la flèche doit être affichée
    if (direction == 1 and tas == 0) or (direction == -1 and tas == nb_tas_global-1):                                               # si on veut aller à gauche et qu'on est sur le premier tas ou si on veut aller à droite et qu'on est sur le dernier tas
        r=[0]                                                                                                                       # on ne fait rien
    for i in r:                                                                                                                     # pour chaque tas
        turtle.goto(coord[0],coord[1]+140*i)                                                                                        # place la tortue sur les coordonnées du tas
        turtle.clear()                                                                                                              # enlève le travail de la tortue
        print_personnage(3, 5, turtle)                                                                                              # print la flèche sur le tas sélectionné
        t.update()                                                                                                                  # met à jour l'affichage


def up_down(menu: str,direction: int,turtle=t):
    """fonction pour interagir avec le menu."""
    global whatisselected, mainmenu, other                                                                                          # appelle les variables sotckées dans whatisselected, mainmenu, other
    turtle.up()                                                                                                                     # lève le stylo
    if menu!="singleplayer":                                                                                                        # condition si on se trouve sur le menu joueur       
        old = mainmenu.index(whatisselected) if menu=="mainmenu" else other.index(whatisselected)                                   # stocke l'indice de la sélection
        if menu=="mainmenu":                                                                                                        # si l'on se trouve sur le menu principal
            whatisselected = mainmenu[old-direction] if 0<=old-direction<=3 else mainmenu[old]                                      # change la sélection en fonction de la direction
        elif menu=="credits" or menu=="how to play":                                                                                # si l'on se trouve sur les menus crédits ou how to play 
            if direction == 1:                                                                                                      # si on veut aller en haut
                if whatisselected == "EXIT":                                                                                        # si on est sur exit
                    whatisselected = "GO TO MAIN MENU"                                                                              # on va sur le menu principal
            elif direction==-1:                                                                                                     # si on veut aller en bas
                if whatisselected == "GO TO MAIN MENU":                                                                             # si on est sur le menu principal
                    whatisselected = "EXIT"                                                                                         # on va sur exit
        update_menu(whatisselected,(mainmenu if menu=="mainmenu" else other),turtle)                                                # met à jour le menu
    else:                                                                                                                           # sinon
        global nb_tas_global, tas_selectionne, l_alive, regle_global, turtle_compteur, over, deathmenu                              # appelle les variables stockées dans les varaibles   
        if over:                                                                                                                    # si le jeu est terminé
            if direction==1:                                                                                                        # si on veut aller en haut
                if whatisselected == "EXIT":                                                                                        # si on est sur exit
                    whatisselected = "GO TO MAIN MENU"                                                                              # on va sur le menu principal
                else:                                                                                                               # sinon  
                    whatisselected = "PLAY AGAIN"                                                                                   # on va sur play again
            elif direction==-1:                                                                                                     # si on veut aller en bas
                if whatisselected == "PLAY AGAIN":                                                                                  # si on veut sélectionner relancer une partie 
                    whatisselected = "GO TO MAIN MENU"                                                                              # si on veut retourner au menu principal
                else:                                                                                                               # sinon
                    whatisselected = "EXIT"                                                                                         # si on veut fermer la page 
            update_menu(whatisselected,deathmenu,turtle)                                                                            # permet de changer de menu 
        old = tas_selectionne                                                                                                       # stocke la sélection précédente
        if l_alive[old[0]]==sum(l_alive):                                                                                           # si il ne reste plus qu'un tas
            return None                                                                                                             # on ne fait rien
        new = (tas_selectionne[0]+direction)%nb_tas_global                                                                          # stocke le nouveau tas sélectionné
        if l_alive[new]<regle_global[0]:                                                                                            # si le tas sélectionné est vide
            ab=abs(direction)                                                                                                       # stocke la valeur absolue de la direction
            return up_down(menu,(direction//ab)*(ab+1) if ab!=0 else 1,turtle)                                                      # on appelle la fonction up_down avec le tas suivant
        if old[1]>l_alive[new]:                                                                                                     # si la règle sélectionnée est plus grande que le tas sélectionné
            u=-1                                                                                                                    # on initialise u à -1
            while l_alive[new]<regle_global[u]:                                                                                     # tant que la règle sélectionnée est plus grande que le tas sélectionné
                u-=1                                                                                                                # on décrémente u
            old=(new,regle_global[u])                                                                                               # on stocke le nouveau tas sélectionné et la nouvelle règle sélectionnée
        tas_selectionne = (new,old[1])                                                                                              # on stocke le nouveau tas sélectionné et la règle sélectionnée
        set_fleche_goomba(tas_selectionne[0],direction,turtle)                                                                      # on rafraichit la fleche
        left_right(0,turtle_compteur)                                                                                               # on rafraichit le compteur


def left_right(direction: int,turtle=t):
    """fonction pour interagir avec le menu."""
    global taille_fenetre, regle_global, l_alive, tas_selectionne
    turtle.up()                                                                                                                     # lève le crayon
    regle_local = [i for i in regle_global if i<=l_alive[tas_selectionne[0]]]                                                       # stocke les règles possibles
    value = tas_selectionne[1]                                                                                                      # stocke la règle sélectionnée
    if value in regle_local:                                                                                                        # si la règle sélectionnée est dans les règles possibles
        ind = regle_local.index(value)                                                                                              # on stocke l'indice de la règle sélectionnée
    else:                                                                                                                           # sinon
        while value not in regle_local and value>-1:                                                                                # tant que la règle sélectionnée n'est pas dans les règles possibles et que la règle sélectionnée est supérieure à -1
            value-=1                                                                                                                # on décrémente la règle sélectionnée
    if value==-1:                                                                                                                   # si la règle sélectionnée == -1 (aucune règle possible)
        return None                                                                                                                 # on ne fait rien
    ind = regle_local.index(value)                                                                                                  # on stocke l'indice de la règle sélectionnée
    whatis = regle_local[ind+direction] if 0<=ind+direction<=len(regle_local)-1 else value                                          # on stocke la nouvelle règle sélectionnée
    tas_selectionne = (tas_selectionne[0],whatis)                                                                                   # on stocke le nouveau tas sélectionné et la nouvelle règle sélectionnée
    turtle.clear()                                                                                                                  # efface le compteur
    text(whatis, 313-taille_fenetre[0]//2,-70+taille_fenetre[1]//2, (255,255,255), "center", 16, "bold",(1,3),t=turtle)             # affiche la nouvelle règle sélectionnée


def update_menu(whatisselected: str,list_menu: list[str], turtle=t):
    """fonction pour mettre à jour le menu."""
    global whatisthemenu, over                                                                                                      # appelle les valeurs stockées dans les variables 
    if whatisthemenu != "singleplayer" or over:                                                                                     # si le menu n'est pas le menu singleplayer ou si la partie est terminée
        ind = list_menu.index(whatisselected)                                                                                       # on stocke l'indice de la valeur sélectionnée
        print_menu = [list_menu[i] for i in range(ind-1,ind+2) if 0<=i<=len(list_menu)-1]                                           # on stocke les valeurs à afficher
        turtle.clear()                                                                                                              # efface le menu
        if ind == 0:                                                                                                                # si la valeur sélectionnée est la première
            text(print_menu[0], 0,-115, (222,88,25), "center", 20, "bold",(1,3),t=turtle)                                           #
            text(print_menu[1], 0,-165, (254,222,201), "center", 18, "normal",(1,3),t=turtle)                                       #
        elif ind == len(list_menu)-1:                                                                                               # si la valeur sélectionnée est la dernière
            text(print_menu[0], 0,-65, (254,222,201), "center", 18, "normal",(1,3),t=turtle)                                        #
            text(print_menu[1], 0,-115, (222,88,25), "center", 20, "bold",(1,3),t=turtle)                                           #
        else:                                                                                                                       # sinon
            text(print_menu[0], 0,-65, (254,222,201), "center", 18, "normal",(1,3),t=turtle)                                        #
            text(print_menu[1], 0,-115, (222,88,25), "center", 20, "bold",(1,3),t=turtle)                                           #
            text(print_menu[2], 0,-165, (254,222,201), "center", 18, "normal",(1,3),t=turtle)                                       #


def select(regle: list[int],nb_tas: int,nb_allumettes_max: int,turtle=t):
    """Fonction pour valider le choix dans le menu ou en jeu."""
    global isgamestarted,whatisselected,whatisthemenu,mainmenu,other, isgamestarted, turtle_fj, turtle_fg, turtle_compteur, over, list_turtle_g, turtle_joueur
    if isgamestarted:                                                                                                               # si le jeu est lancé (menu singleplayer ouvert)
        global l_alive, tas_selectionne, joueur, deathmenu
        for i in range(l_alive[tas_selectionne[0]]-1,l_alive[tas_selectionne[0]]-tas_selectionne[1]-1,-1):                          # pour chaque allumette du tas
            set_goomba(tas_selectionne[0],i,0,list_turtle_g[tas_selectionne[0]][i])                                                 # transforme les goombas en goombas morts
            t.update()                                                                                                              # met à jour l'écran
        l_alive[tas_selectionne[0]]-=tas_selectionne[1]                                                                             # enlève les allumettes du tas
        if sum(l_alive)<regle[0] or (sum(l_alive)==l_alive[tas_selectionne[0]] and 0<l_alive[tas_selectionne[0]]<regle[0]):         # s'il n'y a plus d'allumettes ou plus assez pour jouer
            turtle.clear()                                                                                                          # efface et noircit l'écran
            if 0<sum(l_alive):                                                                                                      # si le joueur ne reussit pas à prendre la dernière allumette, il perd
                joueur = (joueur + 1 )%2                                                                                            # change de joueur
            turtle_compteur.clear()                                                                                                 # efface le compteur
            turtle_fg.clear()                                                                                                       # efface la fleche goomba
            turtle_fj.clear()                                                                                                       # efface le fleche joueur
            turtle_joueur.clear()                                                                                                   # efface les joueur
            if not joueur:                                                                                                          # si c'est le joueur 1 qui a perdu
                turtle_joueur.goto(-taille_fenetre[0]//2,taille_fenetre[1]//2)                                                      # on remplit l'écran de noir
                turtle_joueur.down()                                                                                                # pose le stylo
                turtle_joueur.color((0,0,0))                                                                                        # set la couleur de tracer en noir
                turtle_joueur.begin_fill()                                                                                          # commence le remplissage du tracé 
                turtle_joueur.forward(taille_fenetre[0])                                                                            # avance longueur fenêtre 
                turtle_joueur.right(90)                                                                                             # tourne de 90 
                turtle_joueur.forward(taille_fenetre[1])                                                                            # avance largeur fenêtre 
                turtle_joueur.right(90)                                                                                             # tourne de 90
                turtle_joueur.forward(taille_fenetre[0])                                                                            # avance longueur fenêtre
                turtle_joueur.right(90)                                                                                             # tourne de 9à
                turtle_joueur.forward(taille_fenetre[1])                                                                            # avance largeur fenêtre 
                turtle_joueur.right(90)                                                                                             # tourne 90
                turtle_joueur.end_fill()                                                                                            # fin du remplissage (la page est noire )
                turtle_joueur.goto(-99,66)                                                                                          # place la tortue où on veut afficher le bowser 
                print_personnage(10,6,turtle_joueur)                                                                                # affiche le logo de bowser
            text("Player won!" if joueur else "game over", 0,100, (255,255,255), "center", 24, "bold",(1,3),t=turtle_joueur)        # affiche écran de victoire ou de défaite
            over,isgamestarted = isgamestarted, over                                                                                # le jeu n'est plus lancé
            setpersonnages_joueur(turtle_joueur, (0,joueur))                                                                        # affiche mario selon le joueur qui a gagné
            whatisselected = "PLAY AGAIN"                                                                                           # affiche le menu pour recommencer ou retourner au menu principal
            t.onkey(lambda :up_down(whatisthemenu, 1,turtle), controles["up"])                                                      # déplace la sélection vers le haut
            t.onkey(lambda :up_down(whatisthemenu,-1,turtle), controles["down"])                                                    # déplace la sélection vers le bas
            t.listen()                                                                                                              # écoute les touches
            update_menu(whatisselected, deathmenu, turtle)                                                                          # rafraichit le menu                                                                   
        elif not over:                                                                                                              # sinon si le jeu n'est pas fini
            up_down("singleplayer",0,turtle_fg)                                                                                     # actualise la position de la fleche goomba
            p = sum([i for i in l_alive if i<regle[0]])                                                                             # nombre d'allumettes inaccessibles
            global l_tas
            q = sum([l_tas[i]-l_alive[i] for i in range(len(l_alive)) if l_alive[i]>=regle[0]])                                     # nombre d'allumettes redistribuables
            if p<=q and p>0:                                                                                                        # s'il y a des allumettes inaccessibles et assez de place pour les redistribuer
                for i in range(nb_tas):                                                                                             # pour chaque tas
                    if l_alive[i]<regle[0]:                                                                                         # si le tas est inacessible
                        a = l_alive[i]                                                                                              # nombre d'allumettes dans le tas
                        for j in range(a-1,-1,-1):                                                                                  # pour chaque allumette du tas
                            set_goomba(i,j,0,list_turtle_g[i][j])                                                                   # on affiche un goomba morts
                        l_alive[i]=0                                                                                                # le tas est vide
                        continue                                                                                                    # on passe au tas suivant
                    while l_alive[i]<l_tas[i] and p>0:                                                                              # tant qu'il y a des allumettes à redistribuer
                        set_goomba(i,l_alive[i],1,list_turtle_g[i][l_alive[i]])                                                     # on affiche un goomba vivant
                        l_alive[i]+=1                                                                                               # on ajoute une allumette au tas
                        p-=1                                                                                                        # on enlève une allumette à redistribuer
            left_right(0,turtle_compteur)                                                                                           # actualise le compteur
            joueur = (joueur +1)%2                                                                                                  # change de joueur
            set_fleche_joueur(joueur,turtle_fj)                                                                                     # actualise le joueur
            t.update()                                                                                                              # actualise l'affichage
            if not joueur:                                                                                                          # boucle de jeu de l'ordinateur
                tour_ordi(nb_tas, regle,nb_allumettes_max)                                                                          # tour de l'ordinateur
        return None                                                                                                                 # retourne rien
    if whatisselected=="SINGLEPLAYER":                                                                                              # si on a choisi le mode solo
        whatisthemenu="singleplayer"                                                                                                # on change le menu
    elif whatisselected=="HOW TO PLAY" or whatisselected=="CREDITS":                                                                # si on a choisi le menu "how to play" ou "credits"
        whatisthemenu=whatisselected.lower()                                                                                        # on change le menu
        whatisselected="GO TO MAIN MENU"                                                                                            # on change la sélection
    elif whatisselected=="EXIT":                                                                                                    # si on a choisi le menu "exit"
        t.bye()                                                                                                                     # on ferme la fenêtre
    elif whatisselected=="GO TO MAIN MENU":                                                                                         # si on a choisi le menu "go to main menu"
        if whatisthemenu=="how to play":                                                                                            # si on était dans le menu "how to play"
            global turtle_regle, l_turtle                                                                                           # 
            turtle_regle.clear()                                                                                                    # on efface le menu "how to play"
            turtle_compteur.clear()                                                                                                 # on efface le compteur
            turtle_fj.clear()                                                                                                       # on efface la flèche du joueur
            turtle_fg.clear()                                                                                                       # on efface la flèche du goomba
            for i in l_turtle:                                                                                                      # pour chaque tas
                for j in i:                                                                                                         # pour chaque allumette du tas
                    j.clear()                                                                                                       # on efface l'allumette
        if whatisthemenu=="singleplayer":                                                                                           # si on était dans le menu "singleplayer"
            over=False                                                                                                              # on remet le jeu à zéro
            [turtle_.clear() for i in list_turtle_g for turtle_ in i]                                                               # on efface les goombas
            turtle_joueur.clear()                                                                                                   # on efface la flèche du joueur
        whatisselected=whatisthemenu.upper()                                                                                        # on change la sélection
        whatisthemenu="mainmenu"                                                                                                    # on change le menu
    turtle.clear()                                                                                                                  # on efface la tortue
    turtle.up()                                                                                                                     # on lève le crayon
    loading = t.Turtle()                                                                                                            # on crée une nouvelle tortue de chargement
    loading.hideturtle()                                                                                                            # on cache la tortue de chargement
    loading.up()                                                                                                                    # on lève le crayon
    if whatisthemenu in ["singleplayer","how to play"] and not isgamestarted:                                                       # si on veut aller sur singleplayer ou how to play et que le jeu n'est pas commencé
        if over:                                                                                                                    # si le jeu est terminé
            t.clear()                                                                                                               # efface la tortue 
            [turtle_.clear() for i in list_turtle_g for turtle_ in i]                                                               # efface les goombas
            turtle_joueur.clear()                                                                                                   # efface la flèche du joueur
        hide_title()                                                                                                                # appelle hide title 
        text("LOADING...", taille_fenetre[0]//2-30, -taille_fenetre[1]//2+20, (255,255,255), "right", 24, "bold",(1,3),t=loading)   # affiche le loading de chargement 
        t.update()                                                                                                                  # rafraichir écran avant que fonction soit terminée 
        if whatisthemenu=="singleplayer":                                                                                           # si on veut aller sur singleplayer 
            isgamestarted=True                                                                                                      # on indique qu'on a démarré le jeu 
            over = False                                                                                                            # on indique qu'on a pas fini le jeu
            singleplayer(regle,nb_tas,nb_allumettes_max)                                                                            # appelle singlepayer 
        else:                                                                                                                       # sinon
            menuregle(nb_tas,nb_allumettes_max,regle,turtle=t)                                                                      # appelle menu regle 
        loading.clear()                                                                                                             # efface la tortue loading 
    elif whatisthemenu=="credits":                                                                                                  # si le menu est credits 
        menucredits()                                                                                                               # appelle focntion menucredits( redirige vers menucredits)
    else:                                                                                                                           # sinon
        t.clear()                                                                                                                   # efface la tortue t
    update_menu(whatisselected,(mainmenu if whatisthemenu == "mainmenu" else other),turtle)                                         # appelle le update menu pour aller sur l'interface choisie 
 

def singleplayer(regle: list[int], nb_tas: int, nb_allumettes_max: int) -> None:                
    """Fonction de la boucle du jeu."""
    global joueur, list_turtle_g, turtle_fj, turtle_fg, l_alive, tr, l_tas, tas_selectionne, regle_global, nb_tas_global, turtle_compteur, controles, turtle_joueur
    t.penup()                                                                                                                       # lève le crayon
    l_tas=[randint(regle[0],nb_allumettes_max) for _ in range(nb_tas)]                                                              # liste des tas d'allumettes
    l_alive = l_tas[:]                                                                                                              # liste des goombas vivants (utile pour aficher les morts)
    regle_global = regle[:]                                                                                                         # regle du jeu (utile pour l'exportation en global)
    nb_tas_global = nb_tas                                                                                                          # nombre de tas (utile pour l'exportation en global)
    turtle_fj=t.Turtle()                                                                                                            # creer la turtle pour les fleches de joueurs
    turtle_fg=t.Turtle()                                                                                                            # creer la turtle pour les fleches de goombas
    turtle_compteur=t.Turtle()                                                                                                      # creer la turtle pour le compteur de goombas à enlever
    turtle_fj.hideturtle()                                                                                                          # cache la turtle des fleches de joueurs
    turtle_fg.hideturtle()                                                                                                          # cache la turtle des fleches de goombas
    turtle_compteur.hideturtle()                                                                                                    # cache la turtle du compteur de goombas à enlever
    turtle_joueur=t.Turtle()                                                                                                        # creer la turtle pour les personnages joueurs
    turtle_joueur.hideturtle()                                                                                                      # cache la turtle des personnages joueurs
    turtle_joueur.up()                                                                                                              # leve le crayon de la turtle des personnages joueurs
    setpersonnages_joueur(turtle_joueur)                                                                                            # affiche les personnages joueurs
    list_turtle_g=setpersonnages(l_tas)                                                                                             # affiche les personnages et creer les listes de turtles pour les allumettes
    joueur = 1                                                                                                                      # choisit le joueur 1 pour commencer (1 pour le joueur (mario), 0 pour l'ordi (bowser))
    set_fleche_joueur(joueur,turtle_fj)                                                                                             # affiche la fleche du joueur
    set_fleche_goomba(0,0,turtle_fg)                                                                                                # affiche la fleche du goomba
    tas_selectionne=(0,regle[0])                                                                                                    # initialise le tas selectionne (0) et le nombre d'allumettes a enlever (regle[0])
    text("Goombas à enlever:", -taille_fenetre[0]//2+300, taille_fenetre[1]//2-70, (255,255,255), "right", 16, "bold",(1,3),t=turtle_joueur) # affiche le texte "Goombas à enlever:"
    left_right(0,turtle_compteur)                                                                                                   # affiche le compteur de goombas à enlever
    t.onkey(lambda: up_down(whatisthemenu,1,turtle_fg) if joueur else None, controles["up"])                                        # change la turtle selectionnée
    t.onkey(lambda: up_down(whatisthemenu,-1,turtle_fg) if joueur else None, controles["down"])                                     # pareil
    t.onkey(lambda: left_right(1,turtle_compteur) if joueur else None, controles["right"])                                          # permet de changer la quantité d'allumettes
    t.onkey(lambda: left_right(-1,turtle_compteur) if joueur else None, controles["left"])                                          # pareil
    t.listen()                                                                                                                      # permet d'écouter les nouvelles touches


def tour_ordi(nb_tas, regle,nb_allumettes_max):
    """Fonction qui permet à l'ordinateur de jouer."""
    global turtle_fg, tr, tas_selectionne
    l = [i for i in range(nb_tas) if l_alive[i]>=regle[0]]                                                                          # liste des tas qui ont au moins le nombre d'allumettes minimum pour jouer
    a = l[randint(0,len(l)-1)]                                                                                                      # choisit un tas au hasard
    b = [i for i in regle if i<=l_alive[a]]                                                                                         # liste des nombres d'allumettes que l'ordi peut enlever
    b = b[randint(0,len(b)-1)]                                                                                                      # choisit un nombre d'allumettes au hasard
    while tas_selectionne[0]!=a:                                                                                                    # tant que le tas selectionne n'est pas le bon
        c= 1 if randint(0,1) else -1                                                                                                # choisit un sens de selection
        up_down("singleplayer",c,turtle_fg)                                                                                         # change la fleche de tas
        t.update()                                                                                                                  # actualise l'affichage
        time.sleep(0.4)                                                                                                             # ralentit l'animation de la flèche pour simuler tour ordi
    tas_selectionne = (a,b)                                                                                                         # initialise le tas selectionne (a) et le nombre d'allumettes a enlever (b)
    up_down("singleplayer",0,turtle_fg)                                                                                             # change la fleche de tas
    select(regle,nb_tas,nb_allumettes_max,tr)                                                                                       # enleve les allumettes


def menuregle(nb_tas: int, nb_allumettes_max: int, regle: list[int],turtle=t) -> None:
    """Affiche les regles du jeu."""
    global turtle_regle, turtle_compteur, turtle_fj, turtle_fg, l_turtle, regle_global, l_alive, tas_selectionne, taille_fenetre
    turtle.color(160,172,254)                                                                                                       # couleur de fond
    turtle.up()                                                                                                                     # leve le crayon
    turtle.goto(-250,350)                                                                                                           # va en haut à gauche
    turtle.down()                                                                                                                   # baisse le crayon
    turtle.begin_fill()                                                                                                             # commence le remplissage
    for i in range(4):                                                                                                              # pour chaque coté
        turtle.forward(200+((i+1)%2)*100)                                                                                           # avance de 200 ou 300
        turtle.right(90)                                                                                                            # tourne de 90°
    turtle.end_fill()                                                                                                               # termine le remplissage
    if len(regle) == 1:                                                                                                             # si la regle est de la forme [x]
        texte = str(regle[0]) + " allumette"+ ("s" if regle!=1 else "")                                                             # affiche "1 allumette" ou "x allumettes"
    else:                                                                                                                           # sinon
        texte = ', '.join(map(lambda a: str(a),regle[:-1]))+f" ou {regle[-1]} allumettes"                                           # affiche "x, y ou z allumettes"
    text("regle du jeu :", 0, 255,(254,222,201), "center",24, "normal",(1,3), turtle)                                               # Affiche la règle du jeu
    text(f"Il y a {nb_tas} tas d'allumettes", -350, 225,(254,222,201), "left",16, "normal",(1,3), turtle)                           # affiche nombre de tas d'allumette
    text(f"contenant chacun entre {regle[0]} et {nb_allumettes_max} allumettes:", -350, 195,(254,222,201), "left",16, "normal",(1,3), turtle) #affiche nb allumette contenue dans règle et nombre max allu
    text("Le joueur qui prend la dernière allumette a gagné.", -350, 165,(254,222,201), "left",16, "normal",(1,3), turtle)          # affiche condition de victoire 
    text("Le deuxième joueur est l'ordinateur.", -350, 135,(254,222,201), "left",16, "normal",(1,3), turtle)                        # affiche le fait que l'on joue contre une IA 
    text(f"Un joueur ne peut retirer que {texte} par tour.", -350, 105,(254,222,201), "left",16, "normal",(1,3), turtle)            # le joueur ne peut retirer que nombre allumettes par tour
    text("Un joueur ne peut retirer que des allumettes d'un même tas pendant un tour.", -350, 75,(254,222,201), "left",16, "normal",(1,3), turtle) #
    text("Le joueur qui commence est le joueur 1.", -350, 45,(254,222,201), "left",16, "normal",(1,3), turtle)                      # affiche le fait que joueur 1 commence 
    text("Le jeu utilise les fleches directionnelles.", -350, 15,(254,222,201), "left",16, "normal",(1,3), turtle)                  # affiche commandes directionnelles 
    text("Utilisez les fleches haut/bas pour changer de tas et", -350,-15,(254,222,201), "left",16, "normal",(1,3), turtle)         # pareil 
    text("les fleches gauche/droite pour changer le nombre de goombas selectionné.", -350,-45,(254,222,201), "left",16, "normal",(1,3), turtle)
    turtle.up()                                                                                                                     # lève le crayon 
    turtle_regle=t.Turtle()                                                                                                         # creation d'une tortue exclusive aux regles
    turtle_regle.hideturtle()                                                                                                       # cache cette tortue
    turtle_regle.up()                                                                                                               # leve le crayon
    setpersonnages_joueur(turtle_regle)                                                                                             # affiche les personnages joueur
    l_turtle=setpersonnages([8,2,1,1][:nb_tas])                                                                                     # affiche les goombas
    l_alive = [8,2,0,1][:nb_tas]                                                                                                    # liste des tas non vides
    set_goomba(2,0,0,l_turtle[2][0]) if nb_tas > 2 else set_goomba(0,7,0,l_turtle[0][7])                                            # affiche les goombas
    turtle_fj=t.Turtle()                                                                                                            # creation d'une tortue exclusive aux fleches joueur
    turtle_fj.hideturtle()                                                                                                          # cache cette tortue
    turtle_fj.up()                                                                                                                  # leve le crayon
    turtle_fg=t.Turtle()                                                                                                            # creation d'une tortue exclusive aux fleches goomba
    turtle_fg.hideturtle()                                                                                                          # cache cette tortue
    turtle_fg.up()                                                                                                                  # leve le crayon
    set_fleche_joueur(0,turtle_fj)                                                                                                  # affiche les fleches joueur
    set_fleche_goomba(0,0,turtle_fg)                                                                                                # affiche les fleches goomba
    turtle_compteur=t.Turtle()                                                                                                      # creation d'une tortue exclusive au compteur
    turtle_compteur.hideturtle()                                                                                                    # cache cette tortue
    regle_global = regle[:]                                                                                                         # copie de la regle
    tas_selectionne = (0,regle[0])                                                                                                  # tas selectionné
    text("Goombas à enlever:", -taille_fenetre[0]//2+300, taille_fenetre[1]//2-70, (255,255,255), "right", 16, "bold",(1,3),turtle_regle) # affiche le texte
    left_right(0,turtle_compteur)                                                                                                   # affiche le compteur


def menucredits() -> None:
    """Affiche les credits du jeu."""
    t.clear()                                                                                                                       # efface la tortue 
    t.color(222,88,25)                                                                                                              # set la couleur du panneau (orange)
    t.up()                                                                                                                          # lève le sylo
    t.goto(-190,28)                                                                                                                 # va au coordonnées du haut gauche du panneau 
    t.down()                                                                                                                        # pose le stylo
    t.begin_fill()                                                                                                                  # remplissage
    for _ in range(4):                                                                                                              # boucle 4 fois
        t.forward(381 - 203 * ( _ % 2))                                                                                             # dessine le panneau
        t.left(90)                                                                                                                  # tourne de 90 degrés
    t.end_fill()                                                                                                                    # fin du remplisage 
    text("CREDITS", 0, 90, (254,222,201), "center", 30, "bold",3,t)                                                                 # éciture du texte "CREDIT" centré dans le panneau 
    text("Made by Loïc & Rémi", 0, 40, (254,222,201), "center", 16, "bold",3,t)                                                     # écriture du texte "Made by Loïc & Rémi"centré dans le panneau


def menumain(regle=[1,2,3], nb_tas = 4, nb_allumettes_max = 8) -> None:
    """Fonction pour préparer le jeu. (menu principal)"""
    global isgamestarted, whatisselected, whatisthemenu, mainmenu, other, isgamestarted, tr, over, deathmenu, controle              #
    assert 5 > nb_tas > 0, "Le nombre de tas doit être supérieur à 0."                                                              # vérifie que les paramètres sont corrects
    assert len(regle) > 0, "La regle doit contenir au moins un élément."                                                            #
    regle.sort()                                                                                                                    # trie la regle pour les tests et la simplification des conditions 
    assert regle[0] > 0, "La regle ne doit contenir que des nombres positifs."                                                      # il suffit de vérifier que le premier élément est positif puisque la liste est triée
    assert regle[0] <= nb_allumettes_max, "La regle doit contenir au moins un nombre inférieur ou égal au nombre maximum d'allumettes." # obligatoire pour le randint lors de la création des tas
    mainmenu = ["SINGLEPLAYER", "HOW TO PLAY", "CREDITS", "EXIT"]                                                                   # menu principal
    deathmenu = ["PLAY AGAIN", "GO TO MAIN MENU", "EXIT"]                                                                           # menu de fin de partie
    other = ["GO TO MAIN MENU", "EXIT"]                                                                                             # menu secondaire
    isgamestarted = False                                                                                                           # variable pour vérifier si le jeu est lancé
    over = False                                                                                                                    # variable pour vérifier si le jeu est terminé
    setenv()                                                                                                                        # initialise la fenêtre
    tr=t.Turtle()                                                                                                                   # crée une turtle pour l'affichage des menus
    tr.hideturtle()                                                                                                                 # cache la turtle
    whatisselected="HOW TO PLAY"                                                                                                    # sélectionne le menu "HOW TO PLAY" par défaut
    whatisthemenu="mainmenu"                                                                                                        # affichage du menu principal par défaut
    update_menu(whatisselected,mainmenu,tr)                                                                                         # affiche le menu principal
    try:
        t.onkey(t.bye, controles["echap"])                                                                                          # ferme la fenêtre avec la touche "Escape"
        t.onkey(lambda :up_down(whatisthemenu,1,tr), controles["up"])                                                               # déplace la sélection vers le haut
        t.onkey(lambda :up_down(whatisthemenu,-1,tr), controles["down"])                                                            # déplace la sélection vers le bas
        t.onkey(lambda :select(regle,nb_tas,nb_allumettes_max,tr), controles["enter"])                                              # valide la selection
        t.onkey(toggle_fullscreen, "F11")                                                                                           # active/désactive le mode plein écran
        t.listen()                                                                                                                  # "écoute" les touches définit plus haut
        t.mainloop()                                                                                                                # lance la boucle principale
    except t.Terminator:
        return None


if __name__ == "__main__":                                                                                                          # lance le jeu si le fichier est lancé directement
    regle=[1,2,3]                                                                                                                   # regle par défaut
    nb_tas=4                                                                                                                        # nombre de tas par défaut
    nb_allumettes_max=8                                                                                                             # nombre d'allumettes max par tas par défaut
    menumain(regle,nb_tas,nb_allumettes_max)                                                                                        # lance le jeu, avec les regles par défaut, un nombre de tas aléatoire et le nombre d'allumettes max par défaut
