import pygame
class Setting():
    def __init__(self):
        self.gezi_size = 50
        self.widthx = 1100
        self.heighty = 800
        self.font = pygame.font.Font("img/cao57.ttf",70)
        self.gezi_use = [[0 for i in range(2)]for j in range(196)]
        