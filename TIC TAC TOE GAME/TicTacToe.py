import time
import pygame
import sys
from pygame import mixer


# display for the start screen and paused screen

def start_screen_display(text, text2, text3):
    text_surface = game_font.render(f'{text}', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 120))

    text_surface2 = game_font.render(f'{text2}', True, (255, 255, 255))
    text2_rect = text_surface2.get_rect(center=(200, 200))

    text_surface3 = game_font.render(f'{text3}', True, (255, 255, 255))
    text3_rect = text_surface3.get_rect(center=(200, 300))

    game_screen.blit(text_surface, text_rect)
    game_screen.blit(text_surface2, text2_rect)
    game_screen.blit(text_surface3, text3_rect)


# loads the logo on the start screen


def load_logo_surfaces(logo1, logo2):
    game_screen.blit(logo1, (230, 0))
    game_screen.blit(logo2, (75, 0))


# handles turns to different players each turn....

def check_the_space(turn):
    global current_player
    global mouse_position

    x_o_player = font_forXO.render(current_player, True, (255, 255, 255))

    if turn % 2 == 0:

        current_player = "O"
        x_o_player = font_forXO.render(current_player, True, (255, 0, 0))

    elif turn % 2 != 0:

        current_player = "X"
        x_o_player = font_forXO.render(current_player, True, (0, 0, 0))

    if game_on:
        x_o_rect = x_o_player.get_rect(center=place_x_or_o_at_correct_pos(mouse_position, list_of_coordinates))
        bg_surface.blit(x_o_player, x_o_rect)


# all the possible places a person might click will be corrected ...

def place_x_or_o_at_correct_pos(mouse_pos, li_of_coordinates):
    global counter
    global current_player
    global box1, box2, box3, box4, box5, box6, box7, box8, box9

    if counter % 2 == 0:

        current_player = "O"

    elif counter % 2 != 0:

        current_player = "X"

    if mouse_pos[0] < 133 and mouse_pos[1] < 133:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[0]
        box1 = current_player

    elif 266 > mouse_pos[0] > 133 > mouse_pos[1]:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[1]
        box2 = current_player

    elif mouse_pos[0] > 266 and mouse_pos[1] < 133:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[2]
        box3 = current_player

    elif mouse_pos[0] < 133 < mouse_pos[1] < 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[3]
        box4 = current_player

    elif 133 < mouse_pos[0] < 266 and 133 < mouse_pos[1] < 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[4]
        box5 = current_player

    elif mouse_pos[0] > 266 and mouse_pos[1] > 133 and mouse_pos[1] < 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[5]
        box6 = current_player

    elif mouse_pos[0] < 133 and mouse_pos[1] > 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[6]
        box7 = current_player

    elif 133 < mouse_pos[0] < 266 and mouse_pos[1] > 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[7]
        box8 = current_player

    elif mouse_pos[0] > 266 and mouse_pos[1] > 266:
        mouse_pos[0], mouse_pos[1] = li_of_coordinates[8]
        box9 = current_player

    return mouse_pos


def horizontal_check():
    global game_on
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    global bg_surface

    if box1 == "X" and box2 == "X" and box3 == "X":
        game_on = False
        box1, box2, box3 = "", "", ""

    if box4 == "X" and box5 == "X" and box6 == "X":
        game_on = False
        box1, box2, box3 = "", "", ""

    if box7 == "X" and box8 == "X" and box9 == "X":
        game_on = False
        box1, box2, box3 = "", "", ""

    if box1 == "O" and box2 == "O" and box3 == "O":
        game_on = False
        box1, box2, box3 = "", "", ""

    if box4 == "O" and box5 == "O" and box6 == "O":
        game_on = False
        box1, box2, box3 = "", "", ""

    if box7 == "O" and box8 == "O" and box9 == "O":
        game_on = False
        box1, box2, box3 = "", "", ""


# EXECUTE -

pygame.init()
mixer.init()
mixer.music.load("Assets/sfx_point.wav")
# Setting the volume
mixer.music.set_volume(0.7)

list_of_coordinates = [[66.666, 66.666], [199.99933, 66.666], [333.333366666, 66.666],  # first row
                       [66.666, 199.99933], [199.99933, 199.99933], [333.333366666, 199.99933],  # second row
                       [66.666, 333.33336666], [199.99933, 333.33336666], [333.33336666, 333.33336666]]  # third row

box1, box2, box3, box4, box5, box6, box7, box8, box9 = [str(i) for i in range(1, 10)]  # just a decoy string for each
# box for now

# our surfaces and global variables: ---------------------------------------------------------------


# setting icon
icon_surface = pygame.image.load('Assets/lightning.png')
pygame.display.set_icon(icon_surface)

# setting caption

pygame.display.set_caption("Tic Tac Toe Grid")
pygame.display.set_icon(icon_surface)

# setting logo surfaces
logo_surface = pygame.image.load("Assets/1200px-Tic_tac_toe.svg.png")
logo_surface = pygame.transform.scale(logo_surface, (100, 100))

logo2_surface = pygame.image.load("Assets/EroaQ-5W8AEkUX5.png")
logo2_surface = pygame.transform.scale(logo2_surface, (100, 100))

# setting game screen

game_screen = pygame.display.set_mode((400, 400))
bg_surface = pygame.image.load('Assets/images.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
box_surface = pygame.image.load("Assets/1200px-Solid_white_bordered.svg.png")

# black screen
color = pygame.image.load('Assets/768786f1bda4121b652366c21399a249.png').convert()
color = pygame.transform.scale2x(color)

# fonts
game_font = pygame.font.SysFont("comicsansms", 30)
font_forXO = pygame.font.SysFont("comicsansms", 60)

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
        mouse_position = list(pygame.mouse.get_pos())  # gets all positions of the cursor as game is running
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

                check_the_space(counter)

                if counter < 10:
                    mixer.music.play()
                    # sound only plays when counter is less than

                if counter == 10:  # this sound plays when counter is 10
                    mixer.init()
                    mixer.music.load("Assets/sfx_die.wav")
                    # Setting the volume
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    time.sleep(0.3)

            if event.button == 3:
                game_on = False

    if game_on:  # if game is on, the surface loads, at 0, 0 but if counter goes above 10, game on turns False, and
        # game screen turns black..
        horizontal_check()
        game_screen.blit(bg_surface, (0, 0))
        if counter >= 10:
            game_on = False
            game_screen.blit(color, (0, -100))

    elif not game_on:  # if game on Turns off or is False , The text is displayed AGAIN
        # .... and the cycle continues...
        time.sleep(0.7)
        game_screen.blit(color, (0, -100))
        start_screen_display("Press Space To Start", "Right click to check a box", "Left click to clear grid..")
        load_logo_surfaces(logo_surface, logo2_surface)

        mixer.init()
        mixer.music.load("Assets/sfx_point.wav")
        # Setting the volume
        mixer.music.set_volume(0.7)
        counter = 0

    pygame.display.update()
    clock.tick(60)  # 60 FPS...
