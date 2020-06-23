import pygame
def draw_line(screen,arr,g_set):
    #线框
    pygame.draw.rect(screen, (105,105,105), (100,100,600,600),3)
    #画y轴
    for x in range(100,650,g_set.gezi_size):
        pygame.draw.line(screen, (28,28,28), (x+g_set.gezi_size,100), (x+g_set.gezi_size,700))
    #画x轴
    for y in range(100,650,g_set.gezi_size):
        pygame.draw.line(screen, (105,105,105), (100,y+g_set.gezi_size), (700,y+g_set.gezi_size))
def menu_luozi(screen,renju,g_set):
    #覆盖提示，不然会重叠，参数0填充整个矩形
    pygame.draw.rect(screen, (248,248,255), (780,650,300,100), 0)
    state = g_set.font.render(renju.name + '落子', True, (105,105,105))
    screen.blit(state,(780,650))
    pygame.display.flip() 
import numpy as np
def zuobiao():
    d=np.ones((169,2),int)*100 #创建169个二维矩阵默认值都是100
    d2 = np.arange(100,750,50) #迭代与赋值
    d3 = np.arange(13) * 0 + 100
    for i in range(0,169,13):
        d[i:i+13,1] = d2
        d[i:i+13,0] = d3
        d3 += 50
    return tuple(map(tuple, d)) 
def draw_zuobiao(screen,arr):
    arr2 = []
    for x in arr:
        #绘制每一个坐标并且将rect元素添加到列表
        arr2.append(pygame.draw.circle(screen, (248,248,255), x, 10))
    return arr2
#落子
def play_game(screen,mouse_x,mouse_y,renju,arr3,arr4):
    if renju.color == 'b':
        # bl = pygame.image.load('img/black.png')
        # bl2 = pygame.transform.scale(bl, (20, 20))
        # screen.blit(bl2,(mouse_x,mouse_y) )这里总是对不齐中间坐标所以改用画棋子
        pygame.draw.circle(screen, (0,0,0), (mouse_x,mouse_y), 10)
        print('黑方落子')
        black_decision(renju,mouse_x,mouse_y,arr3)
        renju.name = '白子'
        renju.color = 'w'
    else:
        pygame.draw.circle(screen, (255,255,255), (mouse_x,mouse_y), 10)
        print('白方落子')
        black_decision(renju,mouse_x,mouse_y,arr4)
        renju.name = '黑子'
        renju.color = 'b'
def black_decision(renju,mouse_x,mouse_y,arr3):
    arr3.append((mouse_x,mouse_y))
    #判定黑色左右
    i = 0
    for i in range(5):
        if(mouse_x-50,mouse_y) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_x = mouse_x - 50
        else:
            break
    #判定黑色棋子右边
    for i in range(5):
        if(mouse_x+50,mouse_y) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_x = mouse_x + 50
        else:
            break
    #判定棋子上下
    i = 0
    for i in range(5):
        if(mouse_x,mouse_y+50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y + 50
        else:
            break
    for i in range(5):
        if(mouse_x,mouse_y-50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y - 50
        else:
            break
    #判定倾斜45度
    i = 0
    for i in range(5):
        if(mouse_x+50,mouse_y+50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y + 50
            mouse_x= mouse_x + 50
        else:
            break
    for i in range(5):
        if(mouse_x-50,mouse_y-50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y - 50
            mouse_x= mouse_x - 50
        else:
            break
    #判定倾斜135度
    i = 0
    for i in range(5):
        if(mouse_x + 50,mouse_y - 50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y - 50
            mouse_x= mouse_x + 50
        else:
            break
    for i in range(5):
        if(mouse_x - 50,mouse_y + 50) in arr3:
            i += 1 
            if (i == 4):
                print('黑赢')
                break
            mouse_y= mouse_y + 50
            mouse_x= mouse_x - 50
        else:
            break
def white_decision(renju,mouse_x,mouse_y,arr4):
    arr4.append((mouse_x,mouse_y))
    #判定白色左右
    i = 0
    for i in range(5):
        if(mouse_x-50,mouse_y) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_x = mouse_x - 50
        else:
            break
    #判定白色棋子右边
    for i in range(5):
        if(mouse_x+50,mouse_y) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_x = mouse_x + 50
        else:
            break
    #判定棋子上下
    i = 0
    for i in range(5):
        if(mouse_x,mouse_y+50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y + 50
        else:
            break
    for i in range(5):
        if(mouse_x,mouse_y-50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y - 50
        else:
            break
    #判定倾斜45度
    i = 0
    for i in range(5):
        if(mouse_x+50,mouse_y+50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y + 50
            mouse_x= mouse_x + 50
        else:
            break
    for i in range(5):
        if(mouse_x-50,mouse_y-50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y - 50
            mouse_x= mouse_x - 50
        else:
            break
    #判定倾斜135度
    i = 0
    for i in range(5):
        if(mouse_x + 50,mouse_y - 50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y - 50
            mouse_x= mouse_x + 50
        else:
            break
    for i in range(5):
        if(mouse_x - 50,mouse_y + 50) in arr4:
            i += 1 
            if (i == 4):
                print('白赢')
                break
            mouse_y= mouse_y + 50
            mouse_x= mouse_x - 50
        else:
            break


    