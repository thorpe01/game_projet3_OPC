import pygame


class Seringue(pygame.sprite.Sprite):

    def __init__(self, player):
        super(Seringue, self).__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load("ressource/seringue.png")
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y + 20

    def move(self):
        self.rect.x += self.velocity
