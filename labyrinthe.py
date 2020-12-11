

import pygame
from random import random

class Labyrinthe(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()

        mur = "ressource/mur.png"
        gardien_image = "ressource/Gardien.png"
        liste = "ressource/labyrinthe.txt"

        objet2 = "ressource/ether.png"
        objet3 = "ressource/aiguille.png"
        objet1 = "ressource/tube_plastique.png"

        self.player = player
        self.screen = pygame.display.set_mode((500, 500))
        self.liste = []
        self.objet3 = objet3
        self.objet2 = objet2
        self.objet1 = objet1
        self.mur = mur
        self.gardien_image = gardien_image

        with open(liste) as levels:

            for line in levels:  # For every line in our file
                line = line.strip('\n').split(',')
                # print(line)
                level = []  # We create a another list
                for x in line:
                    # print(x)
                    if x != '\n':
                        level.append(x)
                self.liste.append(line)
        from pprint import pprint
        # pprint(self.liste)


    def generate_tab(self):
        print("init generate_tab")

        for x in range(0, 15):
            # print("line ===>", self.liste[x])
            for y in range(0, 15):
                if self.liste[y][x] == '1':
                    # print(x, y, "égale 1")
                    # print(self.liste[x][y])
                    tuile = pygame.image.load(self.mur).convert_alpha()
                    rect = tuile.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen.blit(tuile, rect)
                if self.liste[y][x] == "S":
                    tuile1 = pygame.image.load(self.gardien_image).convert_alpha()
                    rect = tuile1.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen.blit(tuile1, rect)
                if self.liste[y][x] == "O1":
                    tuile2 = pygame.image.load(self.objet1).convert_alpha()
                    rect = tuile2.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen.blit(tuile2, rect)
                if self.liste[y][x] == "O2":
                    tuile3 = pygame.image.load(self.objet2).convert_alpha()
                    rect = tuile3.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen.blit(tuile3, rect)
                if self.liste[y][x] == "T":
                    tuile4 = pygame.image.load(self.objet3).convert_alpha()
                    rect = tuile4.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen.blit(tuile4, rect)
        # print(len(self.liste), len(self.liste[0]))

        pygame.display.flip()
