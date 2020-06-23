import pygame
class Qipan():
    def __init__(self):
        self.width = 600
        self.height = 600
        self.rect = pygame.Rect(100,100,600,600)
        self.bg = pygame.image.load('img/qipan.jpg').convert_alpha()
    def draw_qipan(self,screen):
        #self.get_rect = pygame.draw.rect(screen, (0,0,0), ((100,100),(600,600)),4)
        screen.fill((248,248,255),self.rect)#填充棋盘
        