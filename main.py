from flask import Flask, request
from uuid import uuid4
import datetime


app = Flask(__name__)

data = {
    "903bc01c08171cc1538532c73a4a353cf1a71ebc": {
        "display_name": "cop",
        "created_at": str(datetime.datetime.now()),
        "email": "copmen81@gmail.com",
        "login": "judas",
        "password": "priest"
        }
}


@app.route('/users',methods=["POST"])
def create_user():
    request_data = request.get_json()
    current_time = str(datetime.datetime.now())
    user_id = str(uuid4())
    new_user = {
        user_id: {
            "display_name": request_data.get("display_name"),
            "created_at": current_time,
            "email": request_data.get("email"),
            "login": request_data.get("login"),
            "password": request_data.get("password")

        }
    }
    data.update(new_user)
    return {
        "id": user_id
    }


@app.route('/users/<user_id>',methods=["GET"])
def get_user(user_id):
    user = data.get(user_id)
    user_inf = {
        "id": user_id,
        "display_name": user.get("display_name"),
        "created_at": user.get("created_at"),
        "email": user.get("email"),
        "login": user.get("login"),
        "password": user.get("password")
    }
    return user_inf


@app.route("/users",methods=["GET"])
def get_users():
    users_list = []
    for key, val in data.items():
        users_list.append({"id": key,
        "display_name": val.get("display_name"),
        "created_at": val.get("created_at"),
        "email": val.get("email"),
        "login": val.get("login"),
        "password": val.get("password")})
    return {
        "users": users_list
    }


@app.route("/users/<user_id>",methods=["DELETE"])
def delete_user(user_id):
    data.pop(user_id)
    return {"success": True}


@app.route("/users/<user_id>",methods=["PATCH"])
def update_user(user_id):
    user = data.get(user_id)
    request_update = request.get_json()
    user["login"] = request_update.get("login")
    user["password"] = request_update.get("password")
    user["display_name"] = request_update.get("display_name")
    user["email"] = request_update.get("email")
    # return {"success": True}
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)