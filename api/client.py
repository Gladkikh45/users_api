import requests
from pprint import pprint
from loguru import logger

logger.add("log.json", format="{time} {level} {message}",
level="INFO", rotation="10 KB", compression="zip", serialize=True)

new_inf = {
    "display_name": "robert",
    "login": "lost",
    "password": "horizon"
}


def create_user():
    url = "http://127.0.0.1:8888/users"
    data = {
        "display_name": "kop",
        "login": "black",
        "password": "sabbath"
    }
    resp = requests.post(url, json=data)
    created_user = resp.text
    print(created_user)


def get_user(user_id):
    url = f"http://127.0.0.1:8888/users/{user_id}"

    resp = requests.get(url)
    user = resp.json()
    print(user)
    

def get_users():
    url = "http://127.0.0.1:8888/users"

    resp = requests.get(url)
    users = resp.json()
    print(users)

def delete_user(user_id):
    url = f"http://127.0.0.1:8888/users/{user_id}"

    resp = requests.delete(url)
    print(resp.status_code)


def update_user(user_id):
    url = f"http://127.0.0.1:8888/users/{user_id}"
    new_inf = {
        "display_name": "robert",
        "login": "lost",
        "password": "horizon"
    }

    resp = requests.patch(url, json=new_inf)


# create_user()
# get_user(user_id="30d55e13-2cdb-424c-9710-f4d3baa69c71")
# delete_user(user_id="63270cbf-ae2b-4fe7-8288-0eb881d690d2")
update_user(user_id="e34359cb-b6cf-4002-b447-be60e36061b9")
get_users()