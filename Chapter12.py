'''Chapter12'''
'''12-1 && 12-2
import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(
        (12000,7500))
    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景色
    bg_color = (41, 174, 255)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        beauty = Beauty(screen)
        beauty.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

class Beauty():
    def __init__(self,screen):
        # 初始化并设置位置
        self.screen = screen

        # 加载图像并获取外接矩形
        self.image = pygame.image.load('images/Beauty.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Beauty放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
run_game()
'''