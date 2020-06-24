class GameStats():
    '''跟踪外星人入侵的统计数据'''
    
    def __init__(self, ai_settings):
        '''初始化统计'''
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 在非活动状态下开始游戏
        self.game_active = False
        
        # 高分不需要重置
        self.high_score = 0
        
    def reset_stats(self):
        '''初始化在游戏中可能会更改的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
