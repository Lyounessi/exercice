# //////////////////////////////////////////////////////////////////
# Effectuer les importations de packages nécessaires pour l'exercice
# //////////////////////////////////////////////////////////////////
import pygame

# /////////////////////////////////////////////////////////
# Ajouter toutes les constantes nécessaires pour l'exercice
# /////////////////////////////////////////////////////////
# ---------
# Constants
# ---------
# -----------
# Window data
# -----------
window_width = 0
window_height = 0
# -----------
# Files paths
# -----------
macgyver_pic = ""
gardian_pic = ""
wall_pic = ""
path_pic = ""
needle_pic = ""
ether_pic = ""
tube_pic = ""


class Game:

    def __init__(self):
        # //////////////////
        # Initialiser Pygame
        # //////////////////
        pass

    def store_map(self):
        # ////////////////////////////////////
        # Stocker le labyrinthe dans une liste
        # ////////////////////////////////////
        pass

    def show_map_console(self):
        # //////////////////////////////////////
        # Afficher le labyrinthe dans la console
        # //////////////////////////////////////
        pass

    def show_map_pygame(self):
        # //////////////////////////////////
        # Afficher le labyrinthe dans pygame
        # //////////////////////////////////
        pass

    def random_pos(self):
        # /////////////////////////////////////////////////////////
        # Positionner les élèments aléatoirement dans le labyrinthe
        # /////////////////////////////////////////////////////////
        pass

class Element:

    def __init__(self):
        # ////////////////////////////////////////////////////////////////////////////////////////////
        # Définir la position initiale et le type d'élèment (éther, aiguille, tube, MacGyver, gardien)
        # ////////////////////////////////////////////////////////////////////////////////////////////
        pass


class Player(Element):

    def __init__(self):
        # //////////////////////////////////////////////////////////////
        # Créer une liste pour stocker les objets collectés par MacGyver
        # //////////////////////////////////////////////////////////////
        Element.__init__(self)
        pass

    def move(self):
        # /////////////////////////////////////
        # Déplacer le joueur dans le labyrinthe
        # /////////////////////////////////////
        pass


if __name__ == "__main__":
    pass


