import time
import pygame
import sys
from pygame import mixer


def start_screen_display(text):
    text_surface = game_font.render(f'{text}\n', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 100))
    game_screen.blit(text_surface, text_rect)


def boxes():
    box_list = [pygame.image.load("Assets/1200px-Solid_white_bordered.svg.png") for i in range(1, 10)]

    for box in box_list:
        box = pygame.transform.scale(box, (120, 120))
        box_rect = box.get_rect(center=mouse_position)
        bg_surface.blit(box, box_rect)


def check_the_space(turn):
    global current_player
    global mouse_position

    x_o_player = game_font_for_XO.render(current_player, True, (255, 255, 255))

    if turn % 2 == 0:
        current_player = "O"
        x_o_player = game_font_for_XO.render(current_player, True, (255, 0, 0))

    elif turn % 2 != 0:
        current_player = "X"
        x_o_player = game_font_for_XO.render(current_player, True, (0, 0, 0))

    if game_on:
        x_o_rect = x_o_player.get_rect(center=tuple(mouse_position))
        bg_surface.blit(x_o_player, x_o_rect)


# EXECUTE -
pygame.init()
mixer.init()
mixer.music.load("Assets/sfx_point.wav")
# Setting the volume
mixer.music.set_volume(0.7)

# our surfaces and global variables: ---------------------------------------------------------------


# setting icon
icon_surface = pygame.image.load('Assets/storm.png')
pygame.display.set_icon(icon_surface)

# setting caption

pygame.display.set_caption("Tic Tac Toe Grid")
pygame.display.set_icon(icon_surface)

# setting game screen

game_screen = pygame.display.set_mode((400, 400))
bg_surface = pygame.image.load('Assets/images.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# black screen
color = pygame.image.load('Assets/768786f1bda4121b652366c21399a249.png').convert()
color = pygame.transform.scale2x(color)

# fonts
game_font = pygame.font.Font('Assets/04B_19.ttf', 30)
game_font_for_XO = pygame.font.Font('Assets/04B_19.ttf', 80)

# clock
clock = pygame.time.Clock()
run = True

# turns true only when space is pressed:
game_on = False

# starts with X mouse pos as None and counter to 0
current_player = "X"
mouse_position = None
counter = 0

# ---------------------------------------------------------------------------------------------------


# GAME LOOP
while run:

    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()  # gets all positions of the cursor as game is running
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # if a key is pressed and it is the space key game runs
            if pygame.K_SPACE:
                game_on = True
                bg_surface = pygame.image.load('Assets/images.png').convert()
                bg_surface = pygame.transform.scale2x(bg_surface)

        if event.type == pygame.MOUSEBUTTONDOWN:  # deploying X and O with the left click
            if event.button == 1 and game_on:
                counter += 1
                boxes()
                check_the_space(counter)

                if counter < 10:
                    mixer.music.play()  # sound only plays when counter is less than

                if counter == 10:  # this sound plays when counter is 10
                    mixer.init()
                    mixer.music.load("Assets/sfx_die.wav")
                    # Setting the volume
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    time.sleep(0.3)

            if event.button == 3:
                start_screen_display("paused")
                game_on = False

    if game_on:  # if game is on, the surface loads, at 0, 0 but if counter goes above 10, game on turns False, and
        # game screen turns black..
        game_screen.blit(bg_surface, (0, 0))
        if counter >= 10:
            game_on = False
            game_screen.blit(color, (0, -100))

    else:  # if game on Turns off or is False , The text is displayed AGAIN .... and the cycle continues...
        mixer.init()
        mixer.music.load("Assets/sfx_point.wav")
        # Setting the volume
        mixer.music.set_volume(0.7)
        counter = 0
        game_screen.blit(color, (0, -100))
        start_screen_display("Press Space To Start")

    pygame.display.update()
    clock.tick(60)  # 60 FPS...
