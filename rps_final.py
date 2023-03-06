# file created by saviorizm
# Goal is to make a game that asks you if you want to play, then give you a choice of rock paper, scissors, or random. then the game displays the result

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# setup  asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 700
HEIGHT = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# list of choices for cpu
choices = ["rock", "paper", "scissors"]

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")
clock = pg.time.Clock()

    # states the path for the rps assets
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
random_image = pg.image.load(os.path.join(game_folder, 'random.jpg')).convert()
intro_image = pg.image.load(os.path.join(game_folder, 'intro_banner.jpg')).convert()
yes_image = pg.image.load(os.path.join(game_folder, 'yes_banner.jpg')).convert()
no_image = pg.image.load(os.path.join(game_folder, 'no_banner.jpg')).convert()
you_and_computer = pg.image.load(os.path.join(game_folder, 'you_and_computer_chose.jpg')).convert()
you_win = pg.image.load(os.path.join(game_folder, 'you_win.jpg')).convert()
you_lose = pg.image.load(os.path.join(game_folder, 'you_lose.jpg')).convert()
you_tie = pg.image.load(os.path.join(game_folder, 'you_tie.jpg')).convert()
image_list = [rock_image, paper_image, scissors_image]


# gets the geometry of the image - the rect version
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
random_rect = random_image.get_rect()
intro_rect = intro_image.get_rect()
yes_rect = yes_image.get_rect()
no_rect = no_image.get_rect()
you_and_computer_rect = you_and_computer.get_rect()
you_win_rect = you_win.get_rect()
you_lose_rect = you_lose.get_rect()
you_tie_rect = you_tie.get_rect()
rect_list = [rock_rect, paper_rect, scissors_rect]

# image coordinates for program
rock_rect.x = 0
paper_rect.y = HEIGHT/2 + 10
scissors_rect.x = WIDTH/2 + 10
random_rect.x = WIDTH/2 + 10
random_rect.y = HEIGHT/2 + 10
yes_rect.y = 500
yes_rect.x = WIDTH/2 - 100
no_rect.y = 500
no_rect.x = 500

# variables that are called later on in code
running = True
intro_displayed = False
player_chose = False
choice_numb = -1
user_choice = ""
computer_image = ""
show_computer_choice = False
current_screen = None
computer_choice_number = randint(0, 2)
computer_choice_name = choices[computer_choice_number]

# blits the "choose screen" - asks the user to make a play choice
def draw_choose_screen():
    screen.fill(BLACK)
    screen.blit(rock_image, rock_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(scissors_image, scissors_rect)
    screen.blit(random_image, random_rect)

# creates function to determine the outome
def compare():
    # allwos us to call the cpu choice in the form of a variable
    # determines if it is a tie
    if user_choice == computer_choice_name:
        print("likewise")
        return "user_tie"
    # checks possibilite for the user chioce rock. if there is no tie(cpu chooses rock) and there is no loss(cpu choice is paper) user is (assumed) to win
    elif user_choice == "rock":
        if computer_choice_name == "scissors":
           return "user_win"
        else:
            return "user_loss"    #    
     # checks possibilite for the user chioce paper. if there is no tie(cpu chooses paper) and there is no loss(cpu choice is scissors) user is (assumed) to win
    elif user_choice == "paper":
        if computer_choice_name == "rock":
            return "user_win"
        else:
            return "user_loss"    #     
            # checks possibilite for the user chioce scissoer. if there is no tie(cpu chooses scissors) and there is no loss(cpu choice is rock) user is (assumed) to win
    elif user_choice == "scissors":
        if computer_choice_name == "paper":
            return "user_win"
        else:
               return "user_loss"
    # else needs to be at the bottom.
    # this happens when the user doesn't give a predetermined response
    else:
        return "try_again"

# function that autonomously runs the final two screens
def final_two_screens():
    # debugging
    print(computer_choice_name)
    print("computer chose " + str(computer_choice_name))
    sleep(1)
    # says "you chose..." and "computer chose..."
    screen.fill(BLACK)
    screen.blit(you_and_computer, you_and_computer_rect)

    # grabs the rect of the copmuter choice
    cpu_image_choice = image_list[computer_choice_number]
    cpu_rect_choice = rect_list[computer_choice_number]
    # placement of the images relative to 0, 0
    cpu_rect_choice.x = WIDTH / 2 + 80
    cpu_rect_choice.y = HEIGHT / 2
    screen.blit(cpu_image_choice, cpu_rect_choice)

# grabs the rect of the player choice
    player_image_choice = image_list[user_choice_number]
    player_rect_choice = rect_list[user_choice_number]
    # placement of the images relative to 0,0
    player_rect_choice.x = 80
    player_rect_choice.y = HEIGHT / 2

# displays the player choice and computer choice
    screen.blit(player_image_choice, player_rect_choice)
    pg.display.flip()
    # satisfies the next requirment.
    current_screen = "result_screen"
    sleep(2)

    # runs a function to check the outcome of the game
    compare_result = compare()
    print(f"compare result is {compare_result}")
    screen.fill(BLACK)
    
    # depending on which otuput the function returned, these lines display the outcome.
    if compare_result == "user_win":
        screen.blit(you_win, you_win_rect)
    elif compare_result == "user_loss":
        screen.blit(you_lose, you_lose_rect)
    elif compare_result == "user_tie":
        screen.blit(you_tie, you_tie_rect)
        # refresh the screen
    pg.display.flip()
    sleep(3)
    pg.quit()

# loop
while running:
    # frames per second
    clock.tick(FPS)
    # each time an event happens
    for event in pg.event.get():
        print("current screen is " + str(current_screen))

        # quits game
        if event.type == pg.QUIT:
            running = False
            # if the user has not chosen whether or not to pla ythe game(automaticallly assumes they havent,
            # it askes them...
        # if the game is just started, display the intro assets
        if current_screen == None:
            # intro()
            # puts the assets on the screen
            screen.fill(BLACK)
            screen.blit(intro_image, intro_rect)
            screen.blit(yes_image, yes_rect)
            screen.blit(no_image, no_rect)
            
            # if the player clicks yes, then continue, if they click no, quit the game
            if event.type == pg.MOUSEBUTTONUP:
                # gets mouse pos when mouse is clicked
                mouse_coords = pg.mouse.get_pos()
                print(mouse_coords)
                # does player want to play?
                if yes_rect.collidepoint(mouse_coords):
                    current_screen = "player_chose"
                    sleep(0.5)
                    draw_choose_screen()
                elif no_rect.collidepoint(mouse_coords):
                    running = False
                else:
                    print("repick")

        if current_screen == "player_chose":
            # calls function that displays the choosing screen
            draw_choose_screen()
            
            # if the player clicks on rock, move on with the code; move onto the next screen and call the final two functions
            if event.type == pg.MOUSEBUTTONUP:
                sleep(.5)
                mouse_coords = pg.mouse.get_pos()
                if rock_rect.collidepoint(mouse_coords):
                    user_choice_number = 0
                    user_choice = "rock"
                    print("you chose " + user_choice)
                    current_screen = "display_computer_choice"
                    final_two_screens()
            # if the player clicks on paper, move on with the code; move onto the next screen and call the final two functions

                elif paper_rect.collidepoint(mouse_coords):
                    user_choice_number = 1
                    user_choice = "paper"
                    print("you chose " + user_choice)
                    current_screen = "display_computer_choice"
                    final_two_screens()

            # if the player clicks on scissors move on with the code; move onto the next screen and call the final two functions
                elif scissors_rect.collidepoint(mouse_coords):
                    user_choice_number = 2
                    user_choice = "scissors"
                    print("you chose " + user_choice)
                    current_screen = "display_computer_choice"
                    final_two_screens()

            # if the player clicks on random, it assigns the user a random choice then moves onto the next screen and call the final two functions
                elif random_rect.collidepoint(mouse_coords):
                    user_choice_number = randint(0,2)
                    user_choice = choices[user_choice_number]
                    print("you chose " + user_choice)
                    current_screen = "display_computer_choice"
                    final_two_screens()

                else:
                    print("where tf u aiming at boa")

    pg.display.flip()

pg.quit()


