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


def add_url(url, link=None, login=None):
    shortened_link = url
    if link is None:
        while True:
            gen_string = generator()
            if not is_shortened_url(gen_string):
                shortened_link = gen_string
                break
    else:
        for url_address in __urls__:
            if url_address.get('link') == link:
                gen_string = generator()
                shortened_link = gen_string
                break
        else:
            shortened_link = link

    new_url = get_link(url, shortened_link, login)
    __urls__.append(new_url)
    save_urls()
    return shortened_link

def get_url(link):
    for user in __urls__:
        if user.get('link') == link:
            return user.get('url')

def get_link(url, link, login):
    return {'url': url, 'link': link, 'login': login}

def is_shortened_url(shortened_link):
    for user in __urls__:
        if user['link'] == shortened_link:
            return True
    return False


def get_list_links(login):
    link_list = []
    for user in __urls__:
        if user.get('login') == login:
            link_list.append(user)
    return link_list

