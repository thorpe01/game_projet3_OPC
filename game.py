import pygame

from gardien import Gardien
from player import Player


class Game:
    def __init__(self, labyrinthe):
        self.invent = []
        self.player = Player()
        self.labyrinthe = labyrinthe
        self.pressed = {}
        self.gardien = Gardien()
        self.objet1 = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        self.objet1 = pygame.transform.scale(self.objet1, (40, 34))
        self.rect = self.objet1.get_rect()
        self.objet2 = pygame.image.load("ressource/ether.png").convert_alpha()
        self.objet2 = pygame.transform.scale(self.objet2, (40, 34))
        self.rect = self.objet2.get_rect()

    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def outils(self):

        if self.player.image == self.objet1:
            self.invent.__add__(self.objet1)
            print("vous avez un item ")
        elif self.player.image == self.objet2:
            self.invent.__add__(self.objet2)
            print("vous avez deux items ")

    def supp(self):
        self.invent.pop()

    def take_objet1(self):
        self.objet1.remove(self.labyrinthe.laby)
        pass

    def take_objet2(self):
        self.objet2.remove(self.labyrinthe.laby)
        pass
