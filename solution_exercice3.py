import pygame
from pygame.locals import *

class Exercices:
    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((560, 560))
        self.mur = pygame.image.load("mur.png").convert()
        self.couloir = pygame.image.load("couloir.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert()
        self.exercice_1()
        self.exercice_2()


    def exercice_1(self):
        """Créer un fichier carte.txt avec les élèments "W", "-" et "M" :
                    WWWWWWWWWWWWWWW
                    WW----M-------W
                    W----WWWWW----W
                    WW--WWWWWWWWW-W
                    WW-----WWWWWWWW
                    WWW----------WW
                    WWWW------WWWWW
                    WWW----W----WWW
                    WW--WWWWW----WW
                    WW----WWWWW---W
                    WWW----------WW
                    WWWW--------WWW
                    WWWWWW----WWWWW
                    WWWWWWWWWWWWWWW
        Ouvrir le fichier carte.txt et ranger les lettres dans une liste à 2 dimensions :
        par exemple, self.carte[1][6] doit être égal à "M"
        Afficher la carte dans la console
        Afficher avec pygame la carte avec les 3 différents sprites (mur, couloir et MacGyver)"""
        element = "WWWWWWWWWWWWWWW\nWW----M-------W\nW----WWWWW----W\nWW--WWWWWWWWW-W\nWW-----WWWWWWWW\nWWW----------WW\nWWWW------WWWWW\nWWW----W----WWW\nWW--WWWWW----WW\nWW----WWWWW---W\nWWW----------WW\nWWWW--------WWW\nWWWWWW----WWWWW\nWWWWWWWWWWWWWWW"
        self.carte = []

        with open("my_map.txt","w") as map:
            map.write(element)

        show = open("my_map.txt","r")
        
        for line in show:
            line = line.rstrip('\n')
            self.carte.append([line])
        #print(self.carte)
        for elt in self.carte:
            for char in elt:
                print(char)

        """Pygame Affichage !"""

        keepon = True

        while keepon:
            for event in pygame.event.get():
                if event.type == QUIT:
                    keepon = False


            #Afficher dans Pygame les sprites a la place des Char dans ma carte

            for elt, value in enumerate(self.carte):
                pos_y = elt *40
                for i, char in enumerate(value[0]):
                    pos_x = 40 * i
                    if char == "W":
                        self.fenetre.blit(self.mur, (pos_x, pos_y))
                    if char == "M":
                        self.fenetre.blit(self.macgyver, (pos_x, pos_y))
                    if char == "-":
                        self.fenetre.blit(self.couloir, (pos_x, pos_y))
                        self.fenetre.blit(self.couloir, (pos_x, pos_y))

            pygame.display.flip()

    def exercice_2(self):
        """
        Demander au joueur de rentrer une lettre : "N", "S", "W" et "E"
        S'il rentre une lettre différente, il faut lui reposer la question
        S'il rentre "N", la lettre "M" se déplace vers la haut dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "S", la lettre "M" se déplace vers la bas dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "E", la lettre "M" se déplace vers la droite dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "W", la lettre "M" se déplace vers la gauche dans la liste à 2 dimensions de l'exercice 1 self.carte
        Puis on repose la question pour un autre mouvement...
        """

        print("Choisir N Pour que M se déplace vers le haut , S vers le bas , E vers la droite, W vers la gauche, et q pour quitter ! ")

        keep = True
        while keep:
            asking = input("Veuiller séléctioner une lettre valide : ")
            if asking == "N":
                pass
            elif asking =="S":
                pass
            elif asking == "E":
                pass
            elif asking == "W":
                pass
            elif asking == "q":
                keep = False
            else:
                print("Lettre invalid")

if __name__ == "__main__":
    exercice = Exercices()
