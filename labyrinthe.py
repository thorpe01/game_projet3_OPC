from random import random

import pygame


class Labyrinthe(pygame.sprite.Sprite):

    def __init__(self, player, gardien, obj1, obj2,obj3, liste,mur):
        super().__init__()
        self.player = player
        self.gardien = gardien
        self.object1 = obj1
        self.object2 = obj2
        self.object3 = obj3
        self.screen = pygame.display.set_mode((500, 500))
        self.liste = liste
        self.mur = mur


    def generate_tab(self):

        x = 0
        y = 0

        tuile = pygame.image.load(self.mur).convert_alpha()

        for i in range(0, 225):
            if self.liste[y][x] == '1':
                self.screen.blit(tuile, (x * 33, y * 33))
            x += 1

            if x == 15:
                x = 0
                y += 1
        pygame.display.flip()
