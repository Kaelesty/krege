from data import db_session
from data.words import Word

import datetime as dt
import random


class Alg:
    def __init__(self, config):
        self.config = config

    def new_word(self, string, article):
        word = Word()
        word.string = string
        word.accent = article
        word.score = 10
        word.register_time = dt.datetime.now()
        db_sess = db_session.create_session()
        db_sess.add(word)
        db_sess.commit()

    def init_words(self):
        db_sess = db_session.create_session()
        """
        0 - за сегодня
        1 - за неделю
        2 - за все время
        """
        words = db_sess.query(Word).filter().all()
        self.map = []
        for word in words:
            self.map += [word] * int(word.score)

    def get_word(self):
        self.last_sended = random.choice(self.map)
        return self.last_sended

    def check_word(self, article):
        db_sess = db_session.create_session()
        word = db_sess.query(Word).filter(Word.string == self.last_sended.string).first()
        if word.accent == article:
            word.score -= self.config["alg-ans-step"] if word.score >= 1 else 0
            db_sess.commit()
            return True
        else:
            word.score += self.config["alg-ans-step"]
            db_sess.commit()
            return False
