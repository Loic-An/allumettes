from random import randint


def questions(question: str, r: (int)):
    """Fonction qui pose une question et vérifie si la réponse est 
    un entier et que celle-ci est dans un intervalle d'entier donné."""
    i = input(question)                                                                             # demande une réponse
    try:
        y = int(i)                                                                                  # vérifie si la réponse est un entier
        assert y in r                                                                               # vérifie si la réponse est dans l'intervalle d'entier donné
        return y                                                                                    # retourne la réponse
    except:                                                                                         # si la réponse n'est pas un entier ou n'est pas dans l'intervalle d'entier donné
        print(f"Veuillez entrer un nombre dans la liste: {', '.join(map(lambda a: str(a),r[:-1]))} ou {règle[-1]}." if len(r) > 1 \
        else f"Veuillez entrer un nombre égal à {r[0]}!")
        return questions(question, r)


def check_tas(nb_tas: int, tas: list, règle: list):
    """Vérifie si il reste des allumettes dans les tas."""
    assert len(tas) == nb_tas, "Le nombre de tas ne correspond pas au nombre de tas donné."
    for i,ta in enumerate(tas):
        if ta==0:
            print("Il ne reste plus d'allumettes dans le tas", i + 1, "!")
            tas.pop(i)
            nb_tas -= 1
        elif ta < règle[0]:                                                                         # si le tas choisi contient moins d'allumettes que la règle minimale
            print(f"Le tas {i+1} ne contient plus assez d'allumettes. \
                \nElles vont être éparpillé dans les autres tas.")
            allu=tas.pop(i)
            nb_tas -= 1
            for i in range(allu):
                tas[randint(0, nb_tas - 1)] += 1                                                    # répartit les allumettes du tas choisi dans les autres tas
            del allu
    return nb_tas, tas


def tour_joueur(nb_tas: int, tas: list, nb_allumettes: int):
    print(f"Il reste {nb_allumettes} allumettes. \nVoici l'état des tas :")                         # affiche le nombre d'allumettes restantes
    for i, nb in enumerate(tas):                                                                    # affiche le nombre d'allumettes restantes dans chaque tas
        print("Tas", i + 1, ":", "I" * nb)
    if nb_tas == 1:                                                                                 # si il ne reste qu'un tas
        print("Il ne reste qu'un tas, il est donc choisi automatiquement.")
        tas_choisi = 1
    else:
        tas_choisi = questions("Choisir un tas: ", range(1, nb_tas + 1))
    règle_tas = [i for i in règle if i <= tas[tas_choisi - 1]]                                      # règle du tas choisi
    nb_allumettes_choisi = questions("Choisir un nombre d'allumettes: ", règle_tas)                 # demande au joueur de choisir un nombre d'allumettes
    tas[tas_choisi - 1] -= nb_allumettes_choisi                                                     # retire le nombre d'allumettes choisi du tas choisi
    return nb_tas,tas, nb_allumettes


def tour_ordi(nb_tas: int, tas: list, nb_allumettes: int):
    tas_choisi = randint(0, nb_tas-1)                                                               # demande au joueur de choisir un tas
    règle_tas = [i for i in règle if i <= tas[tas_choisi - 1]]                                      # règle du tas choisi
    nb_allumettes_choisi = règle_tas[randint(0, len(règle_tas) - 1)]                                # choisit un nombre d'allumettes au hasard
    tas[tas_choisi - 1] -= nb_allumettes_choisi                                                     # retire le nombre d'allumettes choisi du tas choisi
    print(f"L'ordinateur a retiré {nb_allumettes_choisi} allumettes du tas {tas_choisi}.")          # affiche le nombre d'allumettes retirées et le tas choisi
    return nb_tas,tas, nb_allumettes


def game(nb: tuple[int], nb_tas: int, règle: list):
    """Jeu des allumettes. (Niveau 2 ou 3)"""
    assert nb_tas > 0 and len(règle) > 0 and len(nb) == 2 and nb[0] > 0 and nb[1] > 0               # nb_tas > 0: règle non vide; nb est un intervalle d'entier positif
    nb_min, nb_max = sorted(nb)                                                                     # nb_min <= nb_max
    tas = [randint(nb_min, nb_max) for _ in range(nb_tas)]                                          # Création des tas d'allumettes
    règle.sort()                                                                                    # règle est un intervalle d'entier positif croissant
    if len(règle) == 1:                                                                             # corrige l'affichage de la règle en fonction de la longueur de la règle
        t=f"{règle[0]} allumette" if règle[0] == 1 else f"{règle[0]} allumettes" 
    else:
        t=', '.join(map(lambda a: str(a),règle[:-1]))+f" ou {règle[-1]} allumettes"
    print(f"Jeu des allumettes \
            \nRègle du jeu :  \
            \n\tIl y a {nb_tas} tas d'allumettes, \
            \n\tcontentant chacun entre {nb_min} et {nb_max} allumettes: \
            \n\tLe joueur qui prend la dernière allumette a gagné. \
            \n\tLe deuxième joueur est l'ordinateur. \
            \n\tUn joueur ne peut retirer que {t} par tour. \
            \n\tUn joueur ne peut retirer que des allumettes d'un même tas pendant un tour. \
            \n\tLe joueur qui commence est choisi au hasard. \
            \n\tLe jeu commence.")
    joueur = randint(0, 1)                                                                          # joueur = 0: joueur commence; joueur = 1: ordinateur commence
    nb_allumettes = sum(tas)                                                                        # nombre total d'allumettes
    while nb_allumettes > 0:                                                                        # tant qu'il reste des allumettes
        print("C'est au tour", "de l'ordinateur." if joueur else "du joueur.")                      # affiche le joueur qui doit jouer
        nb_tas, tas, nb_allumettes = tour_ordi(nb_tas, tas, nb_allumettes) if joueur else tour_joueur(nb_tas, tas, nb_allumettes) # tour de l'ordinateur ou du joueur
        nb_tas, tas = check_tas(nb_tas, tas, règle)                                                 # vérifie si un tas est vide
        print("Fin du tour","de l'ordinateur." if joueur else "du joueur.")
        joueur = (joueur + 1) % 2                                                                   # change le joueur qui doit jouer
    if joueur:                                                                                      # affiche que le joueur a perdu
        print("Vous avez gagné!")                                                                              
    else:                                                                                          
        print("Vous avez perdu.")                                                         
    return None                                                                                     # fin du jeu


if __name__ == "__main__":
    nb = (1, 10)                                                                                    # nombre d'allumettes par tas
    nb_tas = 3                                                                                      # nombre de tas
    règle = [1, 4, 7]                                                                               # règle du jeu
    game(nb, nb_tas, règle)                                                                         # lance le jeu

