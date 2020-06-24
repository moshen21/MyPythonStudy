import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''管理发射子弹的类'''

    def __init__(self, ai_settings, screen, ship):
        '''创造一个bullet对象，位于现在飞船的位置'''
        super(Bullet, self).__init__()
        self.screen = screen

        # 创造子弹rect在(0, 0),然后设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储子弹位置的小数值
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''在屏幕上移动子弹'''
        # 更新子弹位置小数值
        self.y -= self.speed_factor
        # 更新矩形位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''把子弹展示在屏幕上'''
        pygame.draw.rect(self.screen, self.color, self.rect)
