import pygame


class Labyrinthe(pygame.sprite.Sprite):



    def __init__(self, player, gardien, obj1, obj2):
        super().__init__()
        self.player = player
        self.gardien = gardien
        self.object1 = obj1
        self.object2 = obj2
        self.laby = []
        self.all_mur = pygame.sprite.Group()
        self.image_mur = pygame.image.load("ressource/mur.png")
        self.rect = self.image_mur.get_rect()

    def mur(self):
        self.all_mur.add(self)

    def gener(self):
        self.image_mur = -1
        x_depart = self.player.image
        y_arrive = self.gardien.image
        self.objet2 = 7
        self.objet1 = 8

        self.laby += [[x_depart, -1, -1, -1, -1, -1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, 0, -1, 1, -1, -1]]
        self.laby += [[-1, 0, -1, 0, -1, -1, 0, -1]]
        self.laby += [[-1, -1, -1, 0, -1, 0, 0, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, 0, -1, 0, -1, -1]]
        self.laby += [[-1, 8, 0, 0, -1, 7, 0, -1]]
        self.laby += [[-1, -1, -1, 0, -1, -1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, 0, 0, 0, -1]]
        self.laby += [[-1, 0, -1, -1, 0, -1, 0, -1]]
        self.laby += [[-1, 0, -1, 0, 0, 1, -1, -1]]
        self.laby += [[-1, 0, 0, 0, -1, -1, 0, -1]]
        self.laby += [[-1, -1, -1, 0, 0, 0, 0, y_arrive]]
        self.laby += [[-1, -1, -1, -1, -1, -1, -1, -1]]

        print(self.laby)
            # je choisie une ligne au hasard sauf la première et la dernière
        # detail: je vais choisir un nombre entre 1 et la taille - 2

        # dans ma liste je récupère les index de tout les zeros
        # j'en choisie un au hasard
        # et je le remplace par mon objet
        # et je refais la meme chose pour le second objet


"""if __name__ == '__main__':
    from player import Player
    from gardien import  Gardien

    objet1 = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
    objet1 = pygame.transform.scale(objet1, (40, 34))
    rect = objet1.get_rect()
    objet2 = pygame.image.load("ressource/ether.png").convert_alpha()
    objet2 = pygame.transform.scale(objet2, (40, 34))
    rect = objet2.get_rect()
    player = Player()
    gardien = Gardien()
    Labyrinthe(player,gardien,objet1,objet2).gener()"""

