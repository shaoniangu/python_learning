#__Author__=Youzhi Gu
#Learn Python at Zhejiang University

class Settings():
    def __init__(self):
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)
        self.ship_limit=3

        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=5

        self.drop_speed= 4

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor=0.5
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
