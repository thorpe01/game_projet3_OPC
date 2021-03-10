import random
import time

import pygame


class Labyrinthe:

    def __init__(self,back):
        #super().__init__()

        mur = "ressource/mur.png"
        gardien_image = "ressource/Gardien.png"
        liste = "ressource/labyrinthe.txt"
        objet2 = "ressource/ether.png"
        objet3 = "ressource/aiguille1.png"
        objet1 = "ressource/tube_plastique.png"
        self.back = back
        #self.screen_lab = pygame.display.set_mode((500, 500))
        self.list = []
        self.objet3 = objet3
        self.objet2 = objet2
        self.objet1 = objet1
        self.mur = mur
        self.gardien_image = gardien_image
        self.items = [self.objet1, self.objet2, self.objet3]

        with open(liste) as levels:

            for line in levels:  # For every line in our file
                line = line.strip('\n').split(',')

                level = []  # We create a another list
                for x in line:

                    if x != '\n':
                        level.append(x)
                self.list.append(line)

    def obj_rand(self,back,fond):
        back.blit(fond, (0, 0))

        l = 0
        for x in range(0, 15):
            for y in range(0, 15):
                r = random.randint(1, 15)
                if r == 1 and len(self.items) > l and self.list[y][x] not in ["1",
                                                                              "S"] and x != 0 and y != 0:
                    tuile = pygame.image.load(self.items[l]).convert_alpha()
                    rect = tuile.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    fond.blit(tuile, rect)
                    l += 1
                    pygame.display.update()
                    # self.items.pop(0)


    def generate_tab(self):

        for x in range(0, 15):
            for y in range(0, 15):
                if self.list[y][x] == "1":
                    Mur = pygame.image.load(self.mur).convert_alpha()
                    rect_Mur = Mur.get_rect()
                    rect_Mur.x = x * 33
                    rect_Mur.y = y * 33
                    self.back.blit(Mur, rect_Mur)

                if self.list[y][x] == "S":
                    tuile1 = pygame.image.load(self.gardien_image).convert_alpha()
                    rect = tuile1.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33

                    self.back.blit(tuile1, rect)

                if self.list[y][x] == "O":
                    tuile5 = pygame.image.load(self.back).convert_alpha()
                    rect = tuile5.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.back.blit(tuile5, rect)


                    pygame.display.flip()

