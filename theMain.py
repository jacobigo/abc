
import os
import random
import pygame
from theLogic import *
from theConstants import *


def deal():
    player1 = player()
    print(player1.HP)
    player2 = player()
    print(player2.HP)
    player3 = player()
    print(player3.HP)
    return player1, player2, player3

player1, player2, player3 = deal()
turn = 1

WIDTH, HEIGHT = 800, 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (173, 216, 230)
GREEN = (144, 238, 144)

pygame.display.set_caption("Albanian Card Came")
UPDATER = 60
pygame.font.init()

TITLE_FONT = pygame.font.SysFont('Rowdies', 40)
TITLE_TEXT = TITLE_FONT.render('Keen to a game?', True, (0, 0, 0))

SUBTITLE_FONT = pygame.font.SysFont('Rowdies', 30)
SUBTITLE_TEXT = SUBTITLE_FONT.render('Press Space to start', True, (0, 0, 0))

CARD_IMAGE = pygame.image.load(os.path.join('cardImage.jpg'))
SCALED_CARD = pygame.transform.scale(CARD_IMAGE, (115, 200))

PLAYER2_TEXT = SUBTITLE_FONT.render('Player 2', True, (0, 0, 0))
PLAYER3_TEXT  = SUBTITLE_FONT.render('Player 3', True, (0, 0, 0))



#PLAYER2_HPCARD = pygame.draw.rect(RECT_SURFACE, RED, pygame.rect(30, 30, 60, 60))



def draw_start_screen():
    WINDOW.fill(WHITE)
    WINDOW.blit(TITLE_TEXT, (270, 50))
    WINDOW.blit(SUBTITLE_TEXT, (270, 210))

def draw_game_screen():
    WINDOW.fill(WHITE)
    WINDOW.blit(SCALED_CARD, (340, 25))
    WINDOW.blit(PLAYER2_TEXT, (50, 60))
    WINDOW.blit(PLAYER3_TEXT, (650, 60))
    #player2 HP card
    pygame.draw.rect(WINDOW, RED, pygame.Rect(50, 80, 100, 150))
    #player3 HP card
    pygame.draw.rect(WINDOW, BLUE, pygame.Rect(650, 80, 100, 150))
    #player2 Shield card
    pygame.draw.rect(WINDOW, RED, pygame.Rect(25, 245, 150, 100))
    #player3 Shield card 
    pygame.draw.rect(WINDOW, BLUE, pygame.Rect(625, 245, 150, 100))
    #player1 HP card
    pygame.draw.rect(WINDOW, GREEN, pygame.Rect(350, 350, 100, 150))
    #player1 Shield card
    pygame.draw.rect(WINDOW, GREEN, pygame.Rect(320, 245, 150, 100))

    PLAYER2_HP_REP = SUBTITLE_FONT.render(str(player2.HP), True, (0, 0, 0))
    PLAYER3_HP_REP = SUBTITLE_FONT.render(str(player3.HP), True, (0, 0, 0))
    PLAYER1_HP_REP = SUBTITLE_FONT.render(str(player1.HP), True, (0, 0, 0))

    PLAYER1_SHIELD_REP = SUBTITLE_FONT.render(str(player1.shield), True, (0, 0, 0))
    PLAYER2_SHIELD_REP = SUBTITLE_FONT.render(str(player2.shield), True, (0, 0, 0))
    PLAYER3_SHIELD_REP = SUBTITLE_FONT.render(str(player3.shield), True, (0, 0, 0))

    PLAYER1_CC_REP = SUBTITLE_FONT.render(str('CC: ' + str(player1.chargeCounter)), True, (0, 0, 0))
    PLAYER2_CC_REP = SUBTITLE_FONT.render(str('CC: ' + str(player2.chargeCounter)), True, (0, 0, 0))
    PLAYER3_CC_REP = SUBTITLE_FONT.render(str('CC: ' + str(player3.chargeCounter)), True, (0, 0, 0))

    #HPs
    WINDOW.blit(PLAYER2_HP_REP, (75, 140))
    WINDOW.blit(PLAYER3_HP_REP, (680, 140))
    WINDOW.blit(PLAYER1_HP_REP, (385, 400))
    #Shields
    WINDOW.blit(PLAYER1_SHIELD_REP, (380, 275))
    WINDOW.blit(PLAYER2_SHIELD_REP, (85, 290))
    WINDOW.blit(PLAYER3_SHIELD_REP, (690, 290))
    #Charge Counters
    WINDOW.blit(PLAYER1_CC_REP, (280, 415))
    WINDOW.blit(PLAYER3_CC_REP, (580, 140))
    WINDOW.blit(PLAYER2_CC_REP, (160, 140))

    TURN_TEXT = SUBTITLE_FONT.render(str('Turn: Player ' + str(turn)), True, (0, 0, 0))
    WINDOW.blit(TURN_TEXT, (200, 50))

    pygame.display.flip()


def main():
    
    turn = 1
    clock = pygame.time.Clock()
    run = True
    draw_start_screen()
    while(run):
        clock.tick(UPDATER)
        #pygame.display.flip()

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                print("keydown works")
                if event.key == pygame.K_SPACE:
                    print("key has been pressed")
                    draw_game_screen()
                    

                if(turn == 1):
                    print("Press A to attack Player 2, B to attack Player 3, S to swap your shield, O to swap someone Player 2's shield, K to swap Player 3's shield, or C to charge a card")
                    if event.key == pygame.K_a:
                        print("key a pressed")
                        attack(player1, player2)
                        draw_game_screen()
                    if event.key == pygame.K_b:
                        print("key b pressed")
                        attack(player1, player3)
                        draw_game_screen()
                    if event.key == pygame.K_s:
                        print("key s pressed")
                        swapOwnShield(player1)
                        draw_game_screen()
                    if event.key == pygame.K_o:
                        print("key o was pressed")
                        swapOthersShield(player1, player2)
                        draw_game_screen()
                    if event.key == pygame.K_k:
                        print("key k was pressed")
                        swapOthersShield(player1, player3)
                        draw_game_screen()
                    if event.key == pygame.K_c:
                        print("key c was pressed")
                        charge(player1)
                        draw_game_screen()
                    if(player2.out == True):
                        turn = 3
                    else:
                        turn = 2
                    draw_game_screen()
                    
                
                if(turn == 2):
                    pygame.time.wait(3000)
                    print("Player 2's turn")
                    pygame.time.wait(3000)
                    randomDec = random.randint(1, 6)
                    print(f"randomDec: {randomDec}")
                    if(player3.out == True):
                        randomDec = random.randint(1, 4)
                    
                    if randomDec == 1:
                        print("player 2 attacked player 1")
                        attack(player2, player1)
                        draw_game_screen()
                    if randomDec == 2:
                        print("player 2 charged")
                        charge(player2)
                        draw_game_screen()
                    if randomDec == 3:
                        print("player 2 swapped their shield")
                        swapOwnShield(player2)
                        draw_game_screen()
                    if randomDec == 4:
                        print("player 2 swapped player 1's shield")
                        swapOthersShield(player2, player1)
                        draw_game_screen()
                    if randomDec == 5:
                        print("player 2 swapped player 3's shield")
                        swapOthersShield(player2, player3)
                        draw_game_screen()
                    if randomDec == 6:
                        print("player 2 attacked player 3")
                        attack(player2, player3)
                        draw_game_screen()
                    if(player3.out == True):
                        turn = 1
                    else:
                        turn = 3
                    draw_game_screen()


                if(turn == 3):
                    pygame.time.wait(3000)
                    print("Player 3's turn")
                    pygame.time.wait(3000)
                    randomDec = random.randint(1, 6)
                    print(f"randomDec: {randomDec}")
                    if(player2.out == True):
                        randomDec = random.randint(1, 4)
                    
                    if randomDec == 1:
                        print("player 3 attacked player 1")
                        attack(player3, player1)
                        draw_game_screen()
                    if randomDec == 2:
                        print("player 3 charged")
                        charge(player3)
                        draw_game_screen()
                    if randomDec == 3:
                        print("player 3 swapped their shield")
                        swapOwnShield(player3)
                        draw_game_screen()
                    if randomDec == 4:
                        print("player 3 swapped player 1's shield")
                        swapOthersShield(player3, player1)
                        draw_game_screen()
                    if randomDec == 5:
                        print("player 3 swapped player 2's shield")
                        swapOthersShield(player3, player2)
                        draw_game_screen()
                    if randomDec == 6:
                        print("player 3 attacked player 2")
                        attack(player3, player2)
                        draw_game_screen()
                    turn = 1
                    draw_game_screen()
                        




            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
    pygame.quit()


    


if __name__ == "__main__":
    main()