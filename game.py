import pygame

from gardien import Gardien
from labyrinthe import Labyrinthe
from player import Player


class Game:
    def __init__(self):

        self.init_game()
        self.init_labyrinthe()
        self.init_persos()

    def init_game(self):
        pygame.init()
        pygame.display.set_caption("macgiver")
        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.image.load('ressource/fond.jpg')

        self.pressed = {}

    def init_persos(self):
        self.player = Player(self.labyrinthe.list)
        self.gardien = Gardien()

    def init_labyrinthe(self):
        # print("init labyrinthe")
        self.labyrinthe = Labyrinthe()

    def run(self):

        running = True
        while running:

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image_player, (self.player.rect.x, self.player.rect.y))

            self.player.coup.draw(self.screen)
            self.labyrinthe.generate_tab()

            for seringue in self.player.coup:
                seringue.move()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                    print("fermeture du jeu  ")
                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                if event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
                if self.pressed.get(pygame.K_SPACE) :
                    self.player.use_seringue()
                if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 450:
                    self.player.move_right()
                if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
                    self.player.move_left()
                if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 450:
                    self.player.move_down()
                if self.pressed.get(pygame.K_UP) and self.player.rect.y > 20:
                    self.player.move_up()


