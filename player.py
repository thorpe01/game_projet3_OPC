import pygame

from seringue import Seringue


# création d'une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.health = 10
        self.velocity = 5
        self.attack = 2
        self.coup = pygame.sprite.Group()
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    # attack du player avec la seringue
    # def build_seringue(self):
    # création de la seringue : besoin de l'ether plus une aiguille et un tube
    # récupération de la seringue
    def use_seringue(self):
        self.coup.add(Seringue(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity


