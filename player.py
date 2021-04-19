import pygame

from seringue import Seringue


class Player:

    def __init__(self, lab, back):

        self.image_g_loose = pygame.image.load('ressource/Gardien_loose.png')
        self.rect_loose = self.image_g_loose.get_rect()
        self.image_g_loose = pygame.transform.scale(self.image_g_loose, (30, 30))
        # self.gardien = Gardien()
        self.coup = pygame.sprite.Group()
        self.image_empty = pygame.image.load('ressource/fond.jpg')
        self.rect_empty = self.image_empty.get_rect()
        self.image_empty = pygame.transform.scale(self.image_empty, (30, 30))
        # self.image_wall = pygame.image.load('ressource/mur.png')
        # self.rect_wall = self.image_wall.get_rect()
        # self.image_wall = pygame.transform.scale(self.image_empty, (30, 30))
        self.image_player = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image_player.get_rect()
        self.image_player = pygame.transform.scale(self.image_player, (30, 30))
        self.rect.x = 0  # position init player en x
        self.rect.y = 0  # position init du player en y
        # self.surface = pygame.display.set_mode((500, 500))
        self.lab = lab
        self.back = back
        self.obj_ramasse = set()
        self.count_item = 0
        self.vp = 0

    def use_seringue(self):
        self.coup.add(Seringue(self))

    def move_right(self, items_position):

        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j][i + 1] != "1" and self.lab[j][i + 1] != "S":
            self.rect.x += 33
        if (j, i + 1) in items_position:
            rect_Mur = self.image_empty.get_rect()
            rect_Mur.x = (i + 1) * 33
            rect_Mur.y = j * 33
            self.count_item += 1
            self.obj_ramasse.add((j, i + 1))
            self.back.blit(self.image_empty, rect_Mur)

        if self.lab[j][i + 1] == "S" and self.count_item == 3:
            self.vp += 1

            pygame.display.flip()
            pygame.time.wait(1000)

    def move_left(self, items_position):
        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j][i - 1] != "1":
            self.rect.x -= 33
        if (j, i - 1) in items_position and len(items_position) <= 3:
            rect_Mur = self.image_empty.get_rect()
            rect_Mur.x = (i - 1) * 33
            rect_Mur.y = j * 33
            self.back.blit(self.image_empty, rect_Mur)
            self.count_item += 1
            self.obj_ramasse.add((j, i - 1))
        if self.lab[j][i - 1] == "S" and self.count_item == 3 and self.lab[j][i - 1] != "0":
            self.rect.x -= 33

    def move_up(self, items_position):
        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j - 1][i] != "1":
            self.rect.y -= 33
        if (j - 1, i) in items_position and len(items_position) <= 3:
            rect_Mur = self.image_empty.get_rect()
            rect_Mur.x = i * 33
            rect_Mur.y = (j - 1) * 33
            self.back.blit(self.image_empty, rect_Mur)
            self.count_item += 1
            self.obj_ramasse.add((j - 1, i))

    def move_down(self, items_position):
        i = self.rect.x // 33
        j = self.rect.y // 33
        if self.lab[j + 1][i] != "1":
            self.rect.y += 33
        if (j + 1, i) in items_position:
            rect_Mur = self.image_empty.get_rect()
            rect_Mur.x = i * 33
            rect_Mur.y = (j + 1) * 33
            self.back.blit(self.image_empty, rect_Mur)
            self.count_item += 1
            self.obj_ramasse.add((j + 1, i))
