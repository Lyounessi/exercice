import pygame
from pygame.locals import *

class Exercices:

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((500, 500))
        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert()
        self.exercice_2("W")
        self.exercice_3()
        self.exercice_1()
        pygame.display.flip()#Rafraîchissement de l'écran



    def exercice_1(self):
        """
        Afficher le mot "haut" en console quand on appuie sur la touche fléche vers le haut,
        "bas" quand on appuie sur la touche fléche vers le bas et de même pour les autres
        directions
        """
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        print('Bas')
                elif event.type == KEYUP:
                    if event.key == K_UP:
                        print('Haut')
                    if event.key == K_LEFT:
                        print('Gauche')
                    if event.key == K_RIGHT:
                        print('Droite')
                        
                else:
                    pass
    def exercice_2(self, elt):
        """
        Afficher avec pygame le sprite d'un mur si elt="W" et le sprite de MacGyver
        si elt="M"
        """


        self.elt = input('Taper M pour macgyver et W pour mu : ')
        if self.elt == 'W':
             self.elt = pygame.image.load("mur.png").convert()
             self.fenetre.blit(self.elt, (200,300))
        elif self.elt == 'M':
            self.elt = pygame.image.load("macgyver.png").convert()
            self.fenetre.blit(self.elt, (200,300))
        else:
            print('Not valid')

    def exercice_3(self):
        """
        Afficher avec pygame les sprites suivants "WWWMWMWW"
        """
        self.my_sprites = "WWWMWMWW"
        with open("sprites.txt", "w") as my_file:
            my_file.write(self.my_sprites)
        with open("sprites.txt", "r") as my_file:
            for line in my_file.readlines():



if __name__=="__main__":
    exercice = Exercices()
