from data import db_session


class Alg:
    def __init__(self):
        pass

    def new_word(self, word):
        db_sess = db_session.create_session()
        db_sess.add(word)
        db_sess.commit()