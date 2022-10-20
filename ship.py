import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self,ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        # Присваиваем экран
        self.screen = ai_game.screen
        # Разместить корабль в нужно позиции экрана
        self.screen_rect = ai_game.screen.get_rect()

        #Загружает изобржание корабля и получает прямоугольник
        self.image = pygame.image.load("images/ship.bmp")
        #Позиционирование корабля
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)