import pygame

from gardien import Gardien
from labyrinthe import Labyrinthe
from player import Player


class Game:

    def __init__(self):

        self.init_game()
        self.init_labyrinthe()
        self.init_persos()
        self.victory_count = 0

    def init_game(self):
        pygame.init()
        self.count_party = 0
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

    def quitt_or_retry(self):
        for event in pygame.event.get([pygame.KEYUP, pygame.QUIT]):
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYUP:
                continue
            return event.key
        return None

    def run(self):

        partie = 1
        jouer = True
        # print(f"Cest la PARTIE {partie}")
        while jouer:

            running = True
            # print(f"RUNNING =  {running}")
            while running:
                # print(self.screen.blit(self.player.image_player, (self.player.rect.x, self.player.rect.y)))
                # print("IS RUNNING")
                # print(self.pressed)

                self.screen.blit(self.background, (0, 0))

                self.screen.blit(self.player.image_player, (self.player.rect.x, self.player.rect.y))

                self.player.coup.draw(self.screen)
                self.labyrinthe.generate_tab()

                self.font = pygame.font.Font(None, 30)
                self.text = self.font.render("nombre d'items : " + str(self.player.count_item) + "/3", 1,
                                             (255, 255, 255))

                self.screen.blit(self.text, (250, 10))
                self.font = pygame.font.Font(None, 30)
                self.text = self.font.render("victoire: " + str(self.victory_count), 1,
                                             (255, 255, 255))
                self.screen.blit(self.text, (190, 467))

                pygame.display.flip()

                if (self.player.rect.x // 33 + 1) < len(self.player.lab) and self.player.lab[self.player.rect.y // 33][
                    (self.player.rect.x // 33) + 1] == "S":
                    if self.player.count_item == 3:

                        self.font = pygame.font.Font(None, 50)
                        self.text3 = self.font.render("good job  MAC !  ", 1, (255, 0, 0))
                        self.text = self.font.render("YOU WIN  ", 1, (255, 0, 0))
                        self.screen.blit(self.text, (200, 250))
                        self.screen.blit(self.text3, (150, 100))
                        self.screen.blit(self.gardien.image_g_loose,
                                         (self.gardien.rect_loose.x, self.gardien.rect_loose.y))

                        pygame.display.update()



                    else:

                        self.font1 = pygame.font.Font(None, 30)
                        self.font = pygame.font.Font(None, 50)
                        self.text = self.font.render("GAME OVER ! ", 1, (255, 255, 255))
                        self.text1 = self.font1.render(" DO YOU WANT TO RETRY ?", 1, (255, 255, 255))
                        self.text2 = self.font1.render(" Y " + " OR " + " N ", 1, (255, 255, 255))
                        self.screen.blit(self.text, (150, 200))
                        self.screen.blit(self.text1, (130, 250))
                        self.screen.blit(self.text2, (200, 300))

                        pygame.display.flip()

                # for seringue in self.player.coup:
                # seringue.move()

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        running = False
                        jouer = False

                        print("fermeture du jeu  ")
                    if event.type == pygame.KEYDOWN:
                        self.pressed[event.key] = True

                    if event.type == pygame.KEYUP:
                        self.pressed[event.key] = False

                    if self.pressed.get(pygame.K_y):
                        jouer = True
                        running = False
                        if self.player.count_item == 3:
                            self.victory_count += 1
                        else :
                            self.victory_count -= 1
                        break

                    if self.pressed.get(pygame.K_n):
                        jouer = False
                        running = False

                        break

                    # if self.pressed.get(pygame.K_SPACE):
                    # self.player.use_seringue()
                    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 450:
                        self.player.move_right()
                    if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
                        self.player.move_left()
                    if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 450:
                        self.player.move_down()
                    if self.pressed.get(pygame.K_UP) and self.player.rect.y > 20:
                        self.player.move_up()
                    pygame.display.flip()


            partie += 1
            pygame.display.flip()
            self.init_game()
            self.init_labyrinthe()
            self.init_persos()

        pygame.quit()
