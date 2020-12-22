import pygame

from seringue import Seringue


# création d'une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.coup = pygame.sprite.Group()
        self.image_player = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image_player.get_rect()
        self.image_player = pygame.transform.scale(self.image_player, (30, 30))
        self.rect.x = 0  # position init player en x
        self.rect.y = 0  # position init du player en y


    # attack du player avec la seringue
    # def build_seringue(self):
    # création de la seringue : besoin de l'ether plus une aiguille et un tube
    # récupération de la seringue
    # def use_seringue(self):
    # self.coup.add(Seringue(self))

    def move_right(self):

        self.rect.x += 33

    def move_left(self):
        self.rect.x -= 33

    def move_up(self):
        self.rect.y -= 33

    def move_down(self):
        self.rect.y += 33
