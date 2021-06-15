import pygame

PREFIX = ">>> "


from data import db_session
from data.words import Word
from buttonClass import Button
from tinputClass import Tinput


class UI:
    def __init__(self, alg, config):
        self.running = True
        self.alg = alg
        self.config = config

    def exit(self):
        self.running = False
        self.output("loop closed")


class ConUI(UI):
    def __init__(self, alg, config):
        super().__init__(alg, config)

    def run(self):
        while self.running:
            self.catch_command(input(PREFIX))

    def output(self, text):
        print(PREFIX, text, sep="")

    def catch_command(self, command):
        try:
            exec(f"self.{command}()")
        except Exception as ex:
            self.output(f"exception during process:\n{type(ex)}")
            if type(ex) == AttributeError:
                self.output("вероятно, указанная команда не существует")

    def help(self):
        self.output("""
        \n
        help - помощь по командам
        exit - закрытие цикла/завершение работы
        addWord - добавить слово
        \n
        """)

    def addWord(self):
        self.alg.new_word(Word(
            string=input(f"{PREFIX}слово:\n{PREFIX}"),
            accent=input(f"{PREFIX}ударение:\n{PREFIX}"),
            score=input(f"{PREFIX}рейтинг:\n{PREFIX}")
        ))
        self.output("слово успешно сохранено")


class GUI(UI):
    """
    0 - главное меню
    """
    def __init__(self, alg, config):
        super().__init__(alg, config)
        self.screen = pygame.display.set_mode((self.config["resx"], self.config["resy"]))
        pygame.display.set_caption('Krege!')
        self.clock = pygame.time.Clock()
        self.stat = 0
        self.buttons = []
        self.tinputs = []
        self.init_main_menu()


    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.charged == 1:
                            button.charged = 2
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        if button.charged == 2:
                            if button.under_cursor(pygame.mouse.get_pos()):
                                button.clicked()
                                button.charged = 1
                            else:
                                button.charged = 0
                    for tinput in self.tinputs:
                        if tinput.under_cursor(pygame.mouse.get_pos()):
                            tinput.active = 0 if tinput.active == 1 else 1
                elif event.type == pygame.KEYDOWN:
                    for tinput in self.tinputs:
                        if tinput.active == 1:
                            if event.key != 8:
                                tinput.text += event.unicode
                            elif len(tinput.text) >= 1:
                                tinput.text = tinput.text[:-1]
                else:
                    for button in self.buttons:
                        if button.under_cursor(pygame.mouse.get_pos()):
                            button.charged = 1 if button.charged != 2 else 2
                        elif button.charged != 2:
                            button.charged = 0


            self.draw()
            self.clock.tick(self.config["fps"])
            pygame.display.flip()
        pygame.quit()

    def init_main_menu(self):
        self.reset_ui()
        self.buttons.append(
            Button("Новое слово", (270, 200), self.screen, clicked=self.init_new_word)
        )

    def init_new_word(self):
        self.reset_ui()
        self.tinputs.append(
            Tinput((10, 80), 680, self.screen)
        )
        self.buttons.append(
            Button("Введите слово:", (270, 40), self.screen)
        )
        self.buttons.append(
            Button("Готово ", (310, 120), self.screen, clicked=self.init_set_article)
        )

    def init_set_article(self):
        word = self.tinputs[0].text
        self.reset_ui()
        for i in range(len(word)):
            self.buttons.append(
                Button(word[i], (10 + 30 * i, 120), self.screen, clicked=self.add_word)
            )
        self.buttons.append(
            Button("Выберите ударную гласную: ", (210, 40), self.screen)
        )

    def add_word(self):
        pass


    def reset_ui(self):
        self.buttons, self.tinputs = [], []

    def draw(self):
        for button in self.buttons:
            button.draw()
        for tinput in self.tinputs:
            tinput.draw()
