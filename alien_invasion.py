import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()              #Инициализирует настройки, необходимы Pygame для нормальной работы
        self.settings = Settings() #Создаем экземпляр

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #Доступ к дисплею
        pygame.display.set_caption("Alien Invasion") #Добавление названия игры в верхней части экрана заголовка.
        self.ship = Ship(self)
        #Назначение цвета фона.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            #Отслеживание событий клавиатуры и мыши

    def _check_events(self):
        """Обрабатывает нажатие клавиш и событий мыши"""
        # Не закрыл ли игрок игру нажатием выход
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение на экран и отображает новый экран"""
        #При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()



