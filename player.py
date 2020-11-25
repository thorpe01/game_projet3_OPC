import pygame

from seringue import Seringue


# création d'une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.health = 10
        self.velocity = 1
        self.attack = 2
        self.coup = pygame.sprite.Group()
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15

    # attack du player avec la seringue
    # def build_seringue(self):
    # création de la seringue : besoin de l'ether plus une aiguille et un tube
    # récupération de la seringue
    def use_seringue(self):
        self.coup.add(Seringue(self))

    def recup_objet(self):

        pass

    # utilisation de la seringue
    def move_right(self):
        if not self.collision(self, self.labyrinthe.all_mur):
            self.rect.x += self.velocity
        elif self.collision(self, self.labyrinthe.objet1) or self.collision(self, self.labyrinthe.objet2):
            self.outils()

    def move_left(self):
        if not self.collision(self, self.all_mur):
            self.rect.x -= self.velocity
        elif self.collision(self, self.labyrinthe.objet1) or self.collision(self, self.labyrinthe.objet2):
            self.outils()

    def move_up(self):
        if not self.collision(self, self.all_mur):
            self.rect.y -= self.velocity
        elif self.collision(self, self.labyrinthe.objet1) or self.collision(self, self.labyrinthe.objet2):
            self.outils()

    def move_down(self):
        if not self.collision(self, self.all_mur):
            self.rect.y += self.velocity
        elif self.collision(self, self.labyrinthe.objet1) or self.collision(self, self.labyrinthe.objet2):
            self.outils()

    def outils(self):

        if self.image == self.labyrinthe.objet1:
            self.init_game.invent.__add__(self.labyrinthe.objet1)
            print("vous avez un item ")
            self.init_game.invent.__add__(self.labyrinthe.objet2)
            print("vous avez deux items ")
