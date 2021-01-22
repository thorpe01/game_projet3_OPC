import pygame


class Gardien(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image_gardien = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image_gardien.get_rect()
        self.image_gardien = pygame.transform.scale(self.image_gardien, (33, 33))
        self.rect.x = 470
        self.rect.y = 460
        self.image_g_loose = pygame.image.load('ressource/Gardien_loose.png')
        self.rect_loose = self.image_g_loose.get_rect()
        self.image_g_loose = pygame.transform.scale(self.image_g_loose, (30, 30))
        self.rect_loose.x = 464
        self.rect_loose.y = 434
