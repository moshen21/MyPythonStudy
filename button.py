import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        '''初始换按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # 构建按钮的矩阵对象，并将其居中。
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 该按钮消息仅需要准备一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将msg转换为渲染的图像，并将文本居中放置在按钮上'''
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # 绘制空白按钮，然后绘制消息
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
