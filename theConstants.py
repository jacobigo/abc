import random
import os
import pygame


#initialize player's health and shields
class player:
    HP = -1
    shield = -3
    ammo = 0
    chargeCounter = 0
    out = False
    
    def __init__(self):
        self.HP = random.randint(2, 14) + random.randint(2, 14)
        self.shield = random.randint(2, 14)
        self.chargeCounter = 0
        self.out = False





