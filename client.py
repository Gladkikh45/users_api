import requests


def create_user():
    url = "http://127.0.0.1:8888/users"
    data = {
        "display_name": "kop"
    }
    resp = requests.post(url, json=data)
    created_user = resp.json()
    print(created_user)


def get_user():
    url = "http://127.0.0.1:8888/users/cd61c137-0ae0-42e8-a52d-5febe6c6be18"

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

create_user()
# get_user()
# get_users()
delete_user()