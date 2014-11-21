__author__ = 'Akhtyamov Pavel'

import string
import random
FILE_ENCODING = 'utf-8'

__urls__ = {'1':'http://google.com'}


def generator(size = 6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def add_url(url):
    while True:
        gen_string = generator()
        if __urls__.get(gen_string) is None:
            __urls__[gen_string] = url
            return gen_string

def get_url(hash):
    if __urls__.get(hash) is None:
        return None
    return __urls__[hash]