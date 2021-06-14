from kregeClass import ConUI
from algKlass import Alg

from data import db_session
from data.words import Word

import json


def main():
    app = ConUI(Alg(), load_config())
    app.run()


def load_config():
    config = {
        "debug": True,
        "resx": 600,
        "resy": 300
    }
    try:
        with open("config.json", "r") as configFile:
            new_config = json.load(configFile)
            for key in new_config.keys():
                config[key] = new_config[key]
    except FileNotFoundError:
        print(">>> config.json не найден, используется стандартная конфигурация")
    return config


if __name__ == '__main__':
    db_session.global_init("db/data.sqlite")
    main()