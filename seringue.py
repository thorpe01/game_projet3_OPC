import pygame


class Seringue(pygame.sprite.Sprite):

    def __init__(self):
        super(Seringue, self).__init__()
        self.image = pygame.image.load("ressource/seringue.png")
        self.rect = self.image.get_rect()
        self.rect.x = 460
        self.rect.y = 460
