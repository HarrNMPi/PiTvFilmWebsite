import random
from SpinTheWheel import Simplenote as Note


def get_tv():
    tv = Note.get_tv_list()
    random_tv = random.choice(tv)
    return random_tv


def get_film():
    film = Note.get_film_list()
    random_film = random.choice(film)
    return random_film


def get_book():
    book = Note.get_book_list()
    random_book = random.choice(book)
    return random_book

