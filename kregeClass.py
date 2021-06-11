PREFIX = ">>> "


class Krege:
    def __init__(self):
        self.running = True

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
        \n
        """)

    def exit(self):
        self.running = False
        self.output("loop closed")
