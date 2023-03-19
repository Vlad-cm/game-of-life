import pygame
from random import randint
from copy import deepcopy
from screeninfo import get_monitors


cell = 20
w, h = get_monitors()[0].width // cell, get_monitors()[0].height // cell
FPS = 6
life = True


pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode((w * cell, h * cell))
clock = pygame.time.Clock()

next_field = [[0 for i in range(w)] for j in range(h)]
current_field = [[randint(0, 1) for i in range(w)] for j in range(h)]


def check_cell(field, x, y):
    count = 0

    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if field[i][j]:
                count += 1

    if field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            exit()
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            life = not life
        mouse_pos = pygame.mouse.get_pos()
        if (event.type == pygame.MOUSEBUTTONDOWN) and pygame.mouse.get_pressed()[0]:            
            current_field[mouse_pos[1] // cell][mouse_pos[0] // cell] = 1
        elif (event.type == pygame.MOUSEBUTTONDOWN) and pygame.mouse.get_pressed()[2]:
            current_field[mouse_pos[1] // cell][mouse_pos[0] // cell] = 0

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            if current_field[j][i]:
                pygame.draw.rect(screen, pygame.Color('white'), (i * cell + 2, j * cell + 2, cell - 2, cell - 2))
            if life:
                next_field[j][i] = check_cell(current_field, i, j)
            else:
                next_field[j][i] = current_field[j][i]

    current_field = deepcopy(next_field)

    print(clock.get_fps())

    pygame.display.flip()
    clock.tick(FPS)
