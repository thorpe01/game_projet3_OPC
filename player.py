import pygame
import time


from seringue import Seringue
from gardien import Gardien


# création d'une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, lab ):
        super().__init__()

        self.image_g_loose = pygame.image.load('ressource/Gardien_loose.png')
        self.rect_loose = self.image_g_loose.get_rect()
        self.image_g_loose = pygame.transform.scale(self.image_g_loose, (30, 30))
        self.gardien = Gardien()
        self.coup = pygame.sprite.Group()
        self.image_empty = pygame.image.load('ressource/fond.jpg')
        self.rect_empty = self.image_empty.get_rect()
        self.image_empty = pygame.transform.scale(self.image_empty, (30, 30))
        self.image_wall = pygame.image.load('ressource/mur.png')
        self.rect_wall = self.image_wall.get_rect()
        self.image_wall= pygame.transform.scale(self.image_empty, (30, 30))
        self.image_player = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image_player.get_rect()
        self.image_player = pygame.transform.scale(self.image_player, (30, 30))
        self.rect.x = 0  # position init player en x
        self.rect.y = 0  # position init du player en y
        self.surface = pygame.display.set_mode((500, 500))
        self.lab = lab
        self.count_item = 0
        self.vp = 0

    def use_seringue(self):
     self.coup.add(Seringue(self))

    def move_right(self):

        i = self.rect.x // 33
        j = self.rect.y // 33

        if self.lab[j][i + 1] != "1" and self.lab[j][i + 1] != "S"  :
            self.rect.x += 33

        if self.lab[j][i + 1] == "O1" or self.lab[j][i + 1] == "O3" or self.lab[j][i + 1] == "O2":
            self.lab[j][i + 1] = self.rect_empty
            self.count_item += 1
        if self.lab[j][i + 1] == "S" and self.count_item == 3:
            self.vp += 1


        if self.count_item == 3 and 350 < self.rect.x < 400:
            self.font = pygame.font.Font(None, 30)
            self.text4 = self.font.render("tu peux utiliser la seringue ", 1, (255, 0, 0))
            self.surface.blit(self.text4, (100, 33))

            pygame.display.flip()

            pygame.time.wait(1000)

    def move_left(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j][i - 1] != "1" :
            self.rect.x -= 33
        if self.lab[j][i - 1] == "O1" or self.lab[j][i - 1] == "O3" or self.lab[j][i - 1] == "O2":
            self.lab[j][i - 1] = self.rect_empty
            self.count_item += 1

        if self.lab[j][i - 1] == "S" and self.count_item == 3 and self.lab[j][i - 1] != "0" :
            self.rect.x -= 33

    def move_up(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j - 1][i] != "1":
            self.rect.y -= 33
        if self.lab[j - 1][i] == "O1" or self.lab[j - 1][i] == "O3" or self.lab[j - 1][i] == "O2":
            self.lab[j - 1][i] = self.rect_empty
            self.count_item += 1

    def move_down(self):
        i = self.rect.x // 33
        j = self.rect.y // 33

        if self.lab[j + 1][i] != "1":
            self.rect.y += 33
        if self.lab[j + 1][i] == "O1" or self.lab[j + 1][i] == "O3" or self.lab[j + 1][i] == "O2":
            self.lab[j + 1][i] = self.rect_empty
            self.count_item += 1


