import pygame
class Button():
    def __init__(self,b_shape,b_frame,b_pos,b_name):
        self.color = (0,0,0)
        self.font_color = (105,105,105)
        self.shape = b_shape
        self.position = b_pos
        self.frame = b_frame
        self.name = b_name
    def draw_button(self,screen,g_button,g_set):
        pygame.draw.rect(screen, (0,0,0), g_button.shape, g_button.frame)
        start = g_set.font.render(g_button.name, False, g_button.font_color)
        screen.blit(start,g_button.position)
        #pygame.display.flip()
            