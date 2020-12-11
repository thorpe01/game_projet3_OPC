import pygame


class Gardien(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.image_gardien = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image_gardien.get_rect()
        self.image_gardien = pygame.transform.scale(self.image_gardien, (33, 33))
        self.rect.x = 470
        self.rect.y = 460

