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
        self.all_mur = pygame.sprite.Group()
        self.pressed = {}

    def init_persos(self):
        self.player = Player()
        self.gardien = Gardien()

    def init_objets(self):
        pass

    def init_labyrinthe(self):
        #print("init labyrinthe")
        self.labyrinthe = Labyrinthe( self.player)

    def refresh_tab(self, object_to_display):
        """Method that refreshes the window to display all relevent images"""
        i = 0
        self.screen.blit(self.background, (0, 0))
        self.labyrinthe.generate_tab()
        while i < len(object_to_display):
            self.screen.blit(object_to_display[i].image,
                             (object_to_display[i].position_x * 36, object_to_display[i].position_y * 36))
            i += 1
        pygame.display.flip()



    def run(self):




        running = True
        while running:

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image_player, self.player.rect)
            self.screen.blit(self.gardien.image_gardien, self.gardien.rect)

            self.player.coup.draw(self.screen)
            self.labyrinthe.generate_tab()

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

                # if (player.rect.x, player.rect.y) == (objet1.rect.x, objet1.rect.y):
                # player.pick_up(objet1)

                # if (player.position_x, player.position_y) == (objet2.position_x, objet2.position_y):
                # player.pick_up(objet2)

                # if (player.position_x, player.position_y) == (objet3.position_x, objet3.position_y):
                # player.pick_up(objet3)

                # inst_laby.refresh_maze(object_to_display)

                # if (mcGyver.position_x, mcGyver.position_y) == (warden.position_x, warden.position_y):
                # game_loop = 0
