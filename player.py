import pygame

from seringue import Seringue


# création d'une classe joueur
class Player(pygame.sprite.Sprite):


    def __init__(self, lab):
        super().__init__()
        self.coup = pygame.sprite.Group()
        self.image_empty = pygame.image.load('ressource/fond.jpg')
        self.rect_empty = self.image_empty.get_rect()
        self.image_empty = pygame.transform.scale(self.image_empty, (30, 30))
        self.image_player = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image_player.get_rect()
        self.image_player = pygame.transform.scale(self.image_player, (30, 30))
        self.rect.x = 0  # position init player en x
        self.rect.y = 0  # position init du player en y
        self.lab = lab
        self.count_item = 0





    # attack du player avec la seringue
    # def build_seringue(self):
    # création de la seringue : besoin de l'ether plus une aiguille et un tube
    # récupération de la seringue
    def use_seringue(self):
        self.coup.add(Seringue(self))

    def move_right(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        print(j, i)
        print(self.lab[j][i])
        if self.lab[j][i + 1] != "1":
            print("not wall")
            self.rect.x += 33
        if self.lab[j][i + 1] == "O1" or self.lab[j][i + 1] == "O3" or self.lab[j][i + 1] == "O2":
            self.lab[j][i + 1] = self.rect_empty
            self.count_item += 1


    def move_left(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        print(j, i)
        print(self.lab[j][i])
        if self.lab[j][i - 1] != "1":
            print("not wall")
            self.rect.x -= 33
        if self.lab[j][i - 1] == "O1" or self.lab[j][i - 1] == "O3" or self.lab[j][i - 1] == "O2":
            self.lab[j][i - 1] = self.rect_empty
            self.count_item += 1


    def move_up(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        #print(j, i)
        #print(self.lab[j][i])
        if self.lab[j - 1][i] != "1":
            #print("not wall")
            self.rect.y -= 33
        if self.lab[j - 1][i] == "O1" or self.lab[j - 1][i] == "O3" or self.lab[j - 1][i] == "O2":
            self.lab[j - 1][i] = self.rect_empty
            self.count_item += 1


    def move_down(self):
        i = self.rect.x // 33
        j = self.rect.y // 33
        print(j, i)
        print(self.lab[j][i])
        if self.lab[j + 1][i] != "1":
            print("not wall")
            self.rect.y += 33
        if self.lab[j + 1][i] == "O1" or self.lab[j + 1][i] == "O3" or self.lab[j + 1][i] == "O2":
            self.lab[j + 1][i] = self.rect_empty
            self.count_item += 1




        print('vous avez :',self.count_item ,' objet dans votre sac ')