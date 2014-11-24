__author__ = 'Akhtyamov Pavel'

import string
import random
FILE_ENCODING = 'utf-8'
DATA_FILE = 'data.txt'

def load_urls():
    with open(DATA_FILE, 'r', encoding=FILE_ENCODING) as data_file:
        return eval(data_file.read())

def save_urls():
    with open(DATA_FILE, 'w', encoding=FILE_ENCODING) as data_file:
        print(repr(__urls__), file=data_file)


__urls__ = load_urls()


def generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def add_url(url):
    while True:
        gen_string = generator()
        if __urls__.get(gen_string) is None:
            __urls__[gen_string] = url
            save_urls()
            return gen_string

def get_url(hash):
    if __urls__.get(hash) is None:
        return None
    return __urls__[hash]

