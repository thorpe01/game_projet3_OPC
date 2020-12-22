import pygame


class Labyrinthe(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        mur = "ressource/mur.png"
        gardien_image = "ressource/Gardien.png"
        liste = "ressource/labyrinthe.txt"

        objet2 = "ressource/ether.png"
        objet3 = "ressource/aiguille1.png"
        objet1 = "ressource/tube_plastique.png"

        #self.player = player
        self.screen_lab = pygame.display.set_mode((500, 500))
        self.list = []
        self.objet3 = objet3
        self.objet2 = objet2
        self.objet1 = objet1
        self.mur = mur
        self.gardien_image = gardien_image
        #self.collision = []
        with open(liste) as levels:

            for line in levels:  # For every line in our file
                line = line.strip('\n').split(',')
                # print(line)
                level = []  # We create a another list
                for x in line:
                    # print(x)
                    if x != '\n':
                        level.append(x)
                self.list.append(line)

        from pprint import pprint
        # pprint(self.liste)

    def generate_tab(self):
        # print("init generate_tab")

        for x in range(0, 15):

            for y in range(0, 15):
                if self.list[y][x] == "1":
                    # print(x, y, "égale 1")
                    # print(self.liste[x][y])
                    Mur = pygame.image.load(self.mur).convert_alpha()
                    rect_Mur = Mur.get_rect()
                    rect_Mur.x = x * 33
                    rect_Mur.y = y * 33
                    #self.collision.append(rect_Mur)
                    self.screen_lab.blit(Mur, rect_Mur)

                if self.list[y][x] == "S":
                    tuile1 = pygame.image.load(self.gardien_image).convert_alpha()
                    rect = tuile1.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33

                    self.screen_lab.blit(tuile1, rect)
                if self.list[y][x] == "O1":
                    tuile2 = pygame.image.load(self.objet1).convert_alpha()
                    rect = tuile2.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen_lab.blit(tuile2, rect)

                if self.list[y][x] == "O2":
                    tuile3 = pygame.image.load(self.objet2).convert_alpha()
                    rect = tuile3.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen_lab.blit(tuile3, rect)

                if self.list[y][x] == "O3":
                    tuile4 = pygame.image.load(self.objet3).convert_alpha()
                    rect = tuile4.get_rect()
                    rect.x = x * 33
                    rect.y = y * 33
                    self.screen_lab.blit(tuile4, rect)

        pygame.display.flip()
