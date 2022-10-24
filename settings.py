class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры."""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        #Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction = 1 обозначает движение вправо;
        #а -1 - влево
        self.fleet_direction = 1

        #Настройки корабля
        self.ship_speed = 2
        self.ship_limit = 3

        #Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
