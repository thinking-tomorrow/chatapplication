import database as db
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def register(username, email, password, repeat_password):
    for x in [username, email, password, repeat_password]:
        if x == '':
            return False
    else:
        if not str(username).isalnum():
            return False
        else:
            if not (re.search(regex, email)):
                return False
            else:
                if db.get_user(username):
                    return False
                else:
                    if password != repeat_password:
                        return False
                    else:
                        db.add_user(username, email, password)
                        return True


def login(username, password):
    data = db.get_user(username)
    if not data:
        return False
    else:
        if data['Password'] != password:
            print("false")
        else:
            print("true")
