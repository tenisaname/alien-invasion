import pygame

class Star(object,ai_game):
    def __init__(self, x, y, yspeed):
        self.colour = (0,0,0)
        self.radius = 1
        self.x = x
        self.y = y
        self.yspeed = yspeed

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.radius)

    def fall(self):
        self.y += self.yspeed

    def check_if_i_should_reappear_on_top(self):
        if self.y >= HEIGHT:
            self.y = 0