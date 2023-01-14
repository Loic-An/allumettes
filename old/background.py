import turtle as t

taille_fenetre = (1440,720)  # taille de la fenêtre
def setenv() -> None:
    """Initialise la fenêtre de jeu."""
    global t, taille_fenetre 
    t.setup(taille_fenetre[0], taille_fenetre[1])       # taille de la fenêtre
    t._Screen._root.iconbitmap(r'star.ico')             # icône de la fenêtre
    t.title("SUPER MARIO ALLUMETTES.")                  # titre de la fenêtre
    t.tracer(0)                                         # désactive l'animation de la tortue (pour gagner en vitesse)
    t.colormode(255)                                    # mode couleur rgb
    t.hideturtle()                                      # cache la tortue
    bt = t.Turtle()                                     # crée une tortue pour le fond
    bt.hideturtle()                                     # cache la tortue
    bt.goto(-taille_fenetre[0]//2,-taille_fenetre[1]//2)# couleur de fond
    bt.down()                                           # baisse le crayon
    bt.color(160,172,254)                               # couleur de fond
    bt.begin_fill()                                     # dessine un rectangle et le rempli
    bt.forward(taille_fenetre[0])                       # 
    bt.left(90)                                         #
    bt.forward(taille_fenetre[1])                       #
    bt.left(90)                                         #
    bt.forward(taille_fenetre[0])                       #
    bt.left(90)                                         #
    bt.forward(taille_fenetre[1])                       #
    bt.left(90)                                         #
    bt.end_fill()                                       # fin du remplissage
    bt.up()                                             # lève le crayon


if __name__ == '__main__':
    setenv()
    t.exitonclick()