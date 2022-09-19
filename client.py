import requests
from pprint import pprint


def create_user():
    url = "http://127.0.0.1:8888/users"
    data = {
        "display_name": "kop",
        "email": "kopchik22@gmail.com",
        "login": "black",
        "password": "sabbath"
    }
    resp = requests.post(url, json=data)
    created_user = resp.json()
    print(created_user)


def get_user():
    url = "http://127.0.0.1:8888/users/903bc01c08171cc1538532c73a4a353cf1a71ebc"

    resp = requests.get(url)
    user = resp.json()

    print(user)


def get_users():
    url = "http://127.0.0.1:8888/users"

    resp = requests.get(url)
    users = resp.json()

    print(users)


def delete_user():
    url = "http://127.0.0.1:8888/users/903bc01c08171cc1538532c73a4a353cf1a71ebc"

    resp = requests.delete(url)
    users = resp.json()

    print(users)


def update_user():
    url = "http://127.0.0.1:8888/users/903bc01c08171cc1538532c73a4a353cf1a71ebc"
    new_inf = {
        "display_name": "robert",
        "email": "leather_rebel@gmail.com",
        "login": "lost",
        "password": "horizon"
    }

    resp = requests.patch(url, json=new_inf)
    users = resp.json()

    pprint(users)

create_user()
# get_user()
# get_users()
# delete_user()
update_user()