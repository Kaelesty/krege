PREFIX = ">>> "


from data import db_session
from data.words import Word


class UI:
    def __init__(self, alg, config):
        self.running = True
        self.alg = alg


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

    def exit(self):
        self.running = False
        self.output("loop closed")

    def addWord(self):
        self.alg.new_word(Word(
            string=input(f"{PREFIX}слово:\n{PREFIX}"),
            accent=input(f"{PREFIX}ударение:\n{PREFIX}"),
            score=input(f"{PREFIX}рейтинг:\n{PREFIX}")
        ))
        self.output("слово успешно сохранено")

    def learn(self):
        self.output()
