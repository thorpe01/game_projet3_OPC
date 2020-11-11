import pygame


class Labyrinthe(pygame.sprite.Sprite):

    def __init__(self, player, gardien, game):
        super(Labyrinthe, self).__init__()
        self.player = player
        self.game = game
        self.gardien = gardien
        self.laby = []
        self.all_mur = pygame.sprite.Group()
        self.image_mur = pygame.image.load("ressource/mur.png")
        self.rect = self.image_mur.get_rect()

    def mur(self):
        self.all_mur.add(self)

    def gener(self):
        self.image_mur = -1
        x_depart = self.player.image
        y_arrive = self.gardien.image
        self.game.objet2 = 7
        self.game.objet1 = 8

        self.laby += [[x_depart, -1, -1, -1, -1, -1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, 0, -1, 1, -1, -1]]
        self.laby += [[-1, 0, -1, 0, -1, -1, 0, -1]]
        self.laby += [[-1, -1, -1, 0, -1, 0, 0, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, 0, -1, 0, -1, -1]]
        self.laby += [[-1, 8, 0, 0, -1, 7, 0, -1]]
        self.laby += [[-1, -1, -1, 0, -1, -1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, -1, 0, -1, 0, -1]]
        self.laby += [[-1, 0, -1, 0, 0, 1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, -1, -1, 0, -1]]
        self.laby += [[-1, -1, -1, 0, 0, 0, 0, y_arrive]]
        self.laby += [[-1, -1, -1, -1, -1, -1, -1, -1]]