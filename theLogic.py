import random
import os
from theConstants import *
from theMain import *


def assignNum(num):
    num = random.randint(2, 14)
    return num

def topCard():
    return random.randint(2, 14)

def deal():
    player1 = player()
    print(player1.HP)
    player2 = player()
    print(player2.HP)
    player3 = player()
    print(player3.HP)


def charge(playerEx):
    carddrawn = topCard()
    playerEx.ammo += carddrawn
    playerEx.chargeCounter += 1
    draw_game_screen()

def attack(attacker, defender):
    attacker.ammo += topCard()
    print("ammo: ")
    print(attacker.ammo)

    netDamage = attacker.ammo - defender.shield
    if netDamage > 0:
        defender.HP -= netDamage
        defender.ammo = 0
        defender.chargeCounter = 0
        print(f"Defender's HP after attack: {defender.HP}")

        if(defender.HP <= 0):
            print("defender is out!")
            defender.out = True

    attacker.ammo = 0
    attacker.chargeCounter = 0
    draw_game_screen()

def swapOwnShield(playerEx):
    carddrawn = topCard()
    print(f"topcard: {carddrawn}")
    playerEx.shield = carddrawn
    draw_game_screen()

def swapOthersShield(swapper, swapped):
    carddrawn = topCard()
    swapped.shield = carddrawn
    draw_game_screen()


