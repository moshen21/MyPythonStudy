'''Chapter12'''
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏、设置及创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #设置背景色
    bg_color = (230, 230, 230)

    #开始游戏主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环都会重绘屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()
if __name__ == '__main__':
    run_game()