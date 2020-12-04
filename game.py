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
        self.objet1 = pygame.transform.scale(self.objet1, (33, 33))
        self.rect = self.objet1.get_rect()
        self.objet2 = pygame.image.load("ressource/ether.png").convert_alpha()
        self.objet2 = pygame.transform.scale(self.objet2, (33, 33))
        self.rect = self.objet2.get_rect()
        self.objet3 = pygame.image.load("ressource/aiguille.png").convert_alpha()
        self.objet3 = pygame.transform.scale(self.objet3, (33, 33))
        self.rect = self.objet3.get_rect()

    def init_labyrinthe(self):
        self.labyrinthe = Labyrinthe(self.player, self.gardien, self.objet1, self.objet2,self.objet3,self.)
        self.labyrinthe.generate_tab()

    def outils(self):

        if self.player.image == self.objet1:
            self.invent.__add__(self.objet1)
            print("vous avez un item ")
        if self.player.image == self.objet2:
            self.invent.__add__(self.objet2)
            print("vous avez deux items ")
        if self.player.image == self.objet3:
            self.invent.__add__(self.objet3)
            print("vous avez trois items ")

    def run(self, player, objet1, objet2, objet3):

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

                #if (player.rect.x, player.rect.y) == (objet1.rect.x, objet1.rect.y):
                    # player.pick_up(objet1)

                #if (player.position_x, player.position_y) == (objet2.position_x, objet2.position_y):
                   # player.pick_up(objet2)

                #if (player.position_x, player.position_y) == (objet3.position_x, objet3.position_y):
                   #player.pick_up(objet3)

                #inst_laby.refresh_maze(object_to_display)

                #if (mcGyver.position_x, mcGyver.position_y) == (warden.position_x, warden.position_y):
                    #game_loop = 0
