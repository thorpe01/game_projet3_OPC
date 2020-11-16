import pygame
from game import Game

pygame.init()

# création d'une fenetre de jeu
pygame.display.set_caption("macgiver")
# injecter l'arrière plan
screen = pygame.display.set_mode((500, 500))
# mise à jour de l'écran
background = pygame.image.load('ressource/fond.jpg')

#
game = Game()

running = True

while running:

    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.gardien.image, game.gardien.rect)
    game.player.coup.draw(screen)

    for seringue in game.player.coup:
        seringue.move()

    pygame.display.flip()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() \
            - 2 * game.gardien.rect.width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 450:
        game.player.move_down()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 20:
        game.player.move_up()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu  ")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.use_seringue()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



            # if event.key == pygame.K_RIGHT:
            # game.player.move_right()
            # if event.key == pygame.K_LEFT:
            # game.player.move_left()
            # if event.key == pygame.K_DOWN:
            # game.player.move_down()
            # if event.key == pygame.K_UP:
            # game.player.move_up()
