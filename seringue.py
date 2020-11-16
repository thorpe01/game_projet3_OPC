import pygame


class Seringue(pygame.sprite.Sprite):

    def __init__(self, player):
        super(Seringue, self).__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load("ressource/seringue.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 460
        self.rect.y = player.rect.y + 460

    def move(self):
        self.rect.x += self.velocity
