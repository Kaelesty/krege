import pygame

class Button:
    def __init__(self, text, position, screen, font_size=20, clicked=False, attribute=None):
        self.text = text

        self.size = ((len(text) + 1) * 12, font_size + 15)

        self.clicked = self.inform if not clicked else clicked

        self.font_size = font_size
        self.position = position
        self.screen = screen
        self.width = 2
        self.charged = False
        self.attribute = attribute

    def draw(self):
        font = pygame.font.Font("20806.ttf", self.font_size)
        text = font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.position[0] + 6, self.position[1] + 4))

        pygame.draw.rect(self.screen, (0, 0, 0), (self.position[0], self.position[1], self.size[0], self.size[1]),
                         width=2)
        if self.charged > 0:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.position[0] + 3, self.position[1] + 3, self.size[0] - 5,
                                                      self.size[1] - 5,), width=1)
        if self.charged == 2:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.position[0] + 5, self.position[1] + 5, self.size[0] - 9,
                                                      self.size[1] - 9,), width=1)

    def inform(self):
        print(">>> ouch")

    def under_cursor(self, mPos):
        checked_x = self.position[0] <= mPos[0] <= self.position[0] + self.size[0]
        checked_y = self.position[1] <= mPos[1] <= self.position[1] + self.size[1]
        return checked_x and checked_y
