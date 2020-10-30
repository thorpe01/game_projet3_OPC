import pygame


class Gardien(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.image = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 470
        self.rect.y = 460

    def loose_party(self):
        self.image.add(Gardien())
