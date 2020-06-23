#project起始时间20200619
import sys
import pygame
from renju import Renju
from function import *
from setting import Setting
from button import Button
from qipan import Qipan
pygame.init()
#设置fps
fps = 30
clock = pygame.time.Clock()
#落子坐标元组集
def game_main():
    g_set = Setting()
    screen = pygame.display.set_mode((g_set.widthx, g_set.heighty))
    screen.fill((248,248,255))
    qipan = Qipan()
    qipan.draw_qipan(screen)#棋盘对象不是serface对象，不同于screen
    g_start = Button(((800,100),(200,100)), 4,(830,110),'开始')
    g_restart = Button(((800,300),(200,100)), 4,(830,310),'重置')
    g_rep = Button(((800,500),(200,100)), 4,(830,510),'悔棋')
    g_start.draw_button(screen,g_start,g_set)
    g_restart.draw_button(screen,g_restart,g_set)
    g_rep.draw_button(screen,g_rep,g_set)
    renjuu = Renju('黑子','b')
    flag = True
    #设定图像尺寸
    #qi = pygame.transform.scale(qipan.bg, (650, 650)) 
    #screen.blit(qi,(80,80))
    #pygame.draw.circle(screen,(0,0,0),(600,400),30)
    arr = zuobiao()#获取所有坐标元组
    arr2 = draw_zuobiao(screen,arr)#得到serface的集合的列表
    draw_line(screen,arr,g_set)
    print(renjuu.name + '先行')
    arr3 = []#落过棋子的坐标将被存放这里
    #创建黑白棋数列，存取元组
    arr_black = []
    arr_white = []
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                for i in range(len(arr2)):#迭代arr2的索引
                    if arr2[i].collidepoint(mouse_x, mouse_y) and arr2[i] not in arr3: #验证鼠标点击的点是否在交点范围
                        arr3.append(arr2[i])
                        (mouse_x, mouse_y) = arr[i] #确保鼠标点击落在交点处
                        print((mouse_x,mouse_y))
                        play_game(screen,mouse_x,mouse_y,renjuu,arr_black,arr_white)
                        flag = False
                        menu_luozi(screen,renjuu,g_set)
                if (flag):#控制台提示落子错误
                    print('落子错误')
                    print(arr3)
        pygame.display.flip()
game_main()

