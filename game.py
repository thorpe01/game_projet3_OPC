import pygame

from gardien import Gardien
from labyrinthe import Labyrinthe
from player import Player


class Game:
    def __init__(self):
        self.init_game()
        self.init_persos()
        self.init_objets()
        self.init_labyrinthe()
        self.all_mur = pygame.sprite.Group()

    def init_game(self):
        pygame.init()
        pygame.display.set_caption("macgiver")
        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.image.load('ressource/fond.jpg')
        self.invent = []
        self.pressed = {}

    def init_persos(self):
        self.player = Player()
        self.gardien = Gardien()

    def init_objets(self):
        self.objet1 = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        self.objet1 = pygame.transform.scale(self.objet1, (40, 34))
        self.rect = self.objet1.get_rect()
        self.objet2 = pygame.image.load("ressource/ether.png").convert_alpha()
        self.objet2 = pygame.transform.scale(self.objet2, (40, 34))
        self.rect = self.objet2.get_rect()


    def init_labyrinthe(self):
        self.labyrinthe = Labyrinthe(self.player, self.gardien, self.objet1, self.objet2)
        self.labyrinthe.gener()

    def init_wall(self):
        pass



    def outils(self):

        if self.player.image == self.objet1:
            self.invent.__add__(self.objet1)
            print("vous avez un item ")
        elif self.player.image == self.objet2:
            self.invent.__add__(self.objet2)
            print("vous avez deux items ")

    def supp(self):
        self.invent.pop()

    def take_objet1(self):
        self.objet1.remove(self.labyrinthe.laby)
        pass

    def take_objet2(self):
        self.objet2.remove(self.labyrinthe.laby)
        pass

    def run(self):
        running = True

        while running:

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.gardien.image, self.gardien.rect)
            self.player.coup.draw(self.screen)

            for seringue in self.player.coup:
                seringue.move()

            pygame.display.flip()

            if self.pressed.get(pygame.K_RIGHT) and \
                    self.player.rect.x + self.player.rect.width < self.screen.get_width() \
                    - 2 * self.gardien.rect.width:
                self.player.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
                self.player.move_left()
            elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 450:
                self.player.move_down()
            elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 20:
                self.player.move_up()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("fermeture du jeu  ")
                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        self.player.use_seringue()
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
