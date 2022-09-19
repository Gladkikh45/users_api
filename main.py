from flask import Flask, request
from uuid import uuid4
import datetime


app = Flask(__name__)

data = {
    "903bc01c08171cc1538532c73a4a353cf1a71ebc": {
        "display_name": "cop", "created_at": str(datetime.datetime.now())
        }
}


@app.route('/users',methods=["POST"])
def create_user():
    request_data = request.get_json()
    current_time = str(datetime.datetime.now())
    user_id = str(uuid4())
    new_user = {
        user_id: {
            "display_name": request_data.get("display_name"), "created_at": current_time
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
        "created_at": user.get("created_at")
    }
    return user_inf


@app.route("/users",methods=["GET"])
def get_users():
    users_list = []
    for key, val in data.items():
        users_list.append({"id": key, "display_name": val.get("display_name"), "created_at": val.get("created_at")})
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
    user.update({"display_name": "robert"})
    print(data)
    return {"success": True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)