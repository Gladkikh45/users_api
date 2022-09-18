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
    url = "http://127.0.0.1:8888/users/666"

    resp = requests.get(url)
    user = resp.json()

    print(user)


def get_users():
    url = "http://127.0.0.1:8888/users"

    resp = requests.get(url)
    users = resp.json()

    print(users)


def delete_user():
    url = "http://127.0.0.1:8888/users/666"

    resp = requests.delete(url)
    users = resp.json()

    print(users)

create_user()
get_user()
# get_users()
# delete_user()