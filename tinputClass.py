import pygame

class Tinput:
    def __init__(self, position, length, screen, font_size=20, active=0, text=""):

        self.size = (length, font_size + 15)

        self.active = active

        self.font_size = font_size
        self.position = position
        self.screen = screen
        self.text = text

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.position[0], self.position[1], self.size[0], self.size[1]),
                         width=2)
        if self.active == 1:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.position[0] + 3, self.position[1] + 3, self.size[0] - 5,
                                                      self.size[1] - 5,), width=1)
        font = pygame.font.Font("20806.ttf", self.font_size)
        text = font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.position[0] + 6, self.position[1] + 4))

    def under_cursor(self, mPos):
        checked_x = self.position[0] <= mPos[0] <= self.position[0] + self.size[0]
        checked_y = self.position[1] <= mPos[1] <= self.position[1] + self.size[1]
        return checked_y and checked_x