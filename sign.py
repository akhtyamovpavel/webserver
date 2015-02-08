import hashlib

__author__ = 'user1'

FILE_ENCODING = 'utf-8'
DATA_FILE = 'users.txt'

SALT1 = 'hfdkjhsdlf u92 f2h 82of rh38'
SALT2 = 'u 2xhu e2 ichr h irhewch rc rwuhc roen k ncf'

def load_users_data():
    with open(DATA_FILE, 'r', encoding=FILE_ENCODING) as data_file:
        return eval(data_file.read())


__user_list__ = load_users_data()

def save_users_data():
    with open(DATA_FILE, 'w', encoding=FILE_ENCODING) as data_file:
        print(repr(__user_list__), file=data_file)

def validate_user(user_in, password):
    for user in __user_list__:
        if user.get('login') == user_in:
            salt_pass = SALT1 + password + SALT2
            hash_id = hashlib.md5()
            hash_id.update(bytes(salt_pass, encoding='utf-8'))
            if hash_id.hexdigest() == user.get('password'):
                return True
            else:
                return False
    return False


def is_registered(login):
    for user in __user_list__:
        if user.get('login') == login:
            return True
    return False


def add_user(login, password):
    data = dict()
    data['login'] = login
    hash_id = hashlib.md5()
    hash_id.update(bytes(SALT1 + password + SALT2, encoding='utf-8'))
    data['password'] = hash_id.hexdigest()
    __user_list__.append(data)
    save_users_data()
