import pygame
from settings import arrayMap, WIDTH, HEIGHT, FPS
from drawboard import draw_board
from player import Player
from enemy import Enemy
from settings import TILE_SIZE

from mainmenu import cutscene, calculate_position
from thefall import cutscene as cutscene2
from theportal import cutscene as cutscene3
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font = pygame.font.SysFont('Roboto', 42)
# set caption
pygame.display.set_caption('Blue\'s Adventure in the Mesozoic Era')

# sprite groups
collide_tiles, noncollide_tiles, powerup_tiles, enemy_group, player_group, player = draw_board(
    arrayMap)


def main():
    cutscene(screen)
    cutscene2(screen)
    cutscene3(screen)

    running = True
    is_paused = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = not is_paused

        if is_paused:
            # draw the pause screen
            screen.blit(font.render('Paused', True, 'red'),
                        calculate_position('Paused', WIDTH / 2, HEIGHT / 2))
            pygame.display.update()
            timer.tick(FPS)
            continue

        screen.fill('black')

        collide_tiles.draw(screen)
        noncollide_tiles.draw(screen)
        powerup_tiles.draw(screen)

        player_group.draw(screen)
        player_group.update()

        enemy_group.draw(screen)
        enemy_group.update(player, arrayMap)

        timer.tick(FPS)
        pygame.display.update()  # update the display

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':  # if the file is run directly
    main()
