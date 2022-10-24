import pygame
from settings import Settings
class Ship():
    """Класс для управления кораблем"""

    def __init__(self,ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        # Присваиваем экран
        self.screen = ai_game.screen
        self.settings = Settings()
        # Разместить корабль в нужно позиции экрана
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #Загружает изобржание корабля и получает прямоугольник
        self.image = pygame.image.load("images/ship.png")
        #Позиционирование корабля
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Обновление атрибута rect на основании self.x
        self.rect.x = self.x
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)