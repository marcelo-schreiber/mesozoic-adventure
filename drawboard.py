import pygame
from random import randint
from enemy import Enemy
from player import Player
from settings import TILE_SIZE

PATH = 0
WALL = 1
INVINCIBLE = 2
ZAWARUDO = 3
PLAYER = 4

# priority of movement path finding
RIGHT_UP = 5
RIGHT_DOWN = 6
LEFT_DOWN = 7

class CollideTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.image.load(
            f'sprites/grass{randint(0, 1)}.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PowerUpTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, type):
        super().__init__()
        self.type_of_powerup = type
        self.image = pygame.image.load(
            f'sprites/{self.type_of_powerup}.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))


class NonCollideTiles(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.image.load(
            f'sprites/dirt{randint(0, 1)}.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def draw_board(level, period):
    # each block should have a width of 30 pixels and a height of 30 pixels
    # (the board should be 30 blocks wide and 30 blocks high)
    # create new sprite group

    name = "ptedoaustro"

    if period == "Triassic":
        name = "eoraptor"
    elif period == "Jurassic":
        name = "yi qi"
    elif period == "Cretaceous":
        name = "ptedoaustro"
    elif period == "Cenozoic":
        name = "queroquero"


    collide_tiles = pygame.sprite.Group()
    noncollide_tiles = pygame.sprite.Group()
    powerup_tiles = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle()
    player = Player(0, 0, 0, None, None, None, None)
    # loop through level array
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == WALL:
                collide_tiles.add(CollideTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'black'))
                continue
            elif level[row][col] == PATH:
                powerup_tiles.add(PowerUpTile(
                    col * TILE_SIZE + (TILE_SIZE/6), row * TILE_SIZE + (TILE_SIZE/6), TILE_SIZE/1.5, TILE_SIZE/1.5, 'scooby'))
            elif level[row][col] == INVINCIBLE:
                powerup_tiles.add(PowerUpTile(
                    col * TILE_SIZE + (TILE_SIZE/6), row * TILE_SIZE + (TILE_SIZE/6), TILE_SIZE/1.5, TILE_SIZE/1.5, 'invinc'))
            elif level[row][col] == RIGHT_UP:
                enemy_group.add(Enemy(name, col * TILE_SIZE,
                                row * TILE_SIZE, TILE_SIZE, 1, 1, 1))
            elif level[row][col] == RIGHT_DOWN:
                enemy_group.add(Enemy(name, col * TILE_SIZE,
                                row * TILE_SIZE, TILE_SIZE, 1, 1, -1))
            elif level[row][col] == LEFT_DOWN:
                enemy_group.add(
                    Enemy(name, col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, 1, -1, -1))
            elif level[row][col] == PLAYER:
                player = Player(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, collide_tiles, powerup_tiles, noncollide_tiles, enemy_group)
                player_group.add(player)

            noncollide_tiles.add(NonCollideTiles(
                col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'white'))

    return collide_tiles, noncollide_tiles, powerup_tiles, enemy_group, player_group, player
