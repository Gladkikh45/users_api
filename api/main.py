from flask import Flask, request
from uuid import uuid4
import datetime
# from configuration.config import get_config
from flask import Response
import json
from logger.logger import get_logger
from database.client import get_cursor

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

# conf = get_config()
# logger = get_logger(file_name=conf["log"]["file_name"])

@app.route('/users',methods=["POST"])
def create_user():
    request_data = request.get_json()

    cursor, conn = get_cursor()

    try:
        cursor.execute(f"""
        INSERT INTO main.users (display_name, login, hash)
        VALUES ('{request_data['display_name']}', '{request_data['login']}', '{request_data['password']}')
        RETURNING id""")
        record = cursor.fetchone()
        conn.commit()
    except Exception as error:
        print(error)


    result_id = {
        'id': record['id'],
    }

    result = json.dumps(result_id)

    return Response(response=result, status=201, mimetype='application/json')


@app.route('/users/<user_id>',methods=["GET"])
def get_user(user_id):
    # logger.info("user_get_information")
    cursor, conn = get_cursor()

    try:
        cursor.execute(f"""
        SELECT id, display_name, created_at, login
        FROM main.users
        WHERE id = '{user_id}';
        """)
        record = cursor.fetchone()
    except Exception as error:
        print(error)

    id_inf = record.get('id')
    dn_inf = record.get('display_name')
    ca_inf = record.get('created_at')
    email_inf = record.get('email')
    login_inf = record.get('login')

    result = {
        "user": {
            'id': id_inf,
            'display_name': dn_inf,
            'created_at': str(ca_inf),
            'email': email_inf,
            'login': login_inf,
        }
        
    }

    response = json.dumps(result)
    return Response(response=response, status=200, mimetype='application/json')


@app.route("/users",methods=["GET"])
def get_users():
    # logger = get_logger(file_name)

    cursor, conn = get_cursor()

    try:
        cursor.execute("SELECT id, display_name FROM main.users")
        records = cursor.fetchall()
    except Exception as error:
        print(error)

    result = {
        "users": []
    }

    for user in records:
        user_id = user.get('id')
        display_name = user.get('display_name')

        item = {
            'id': user_id,
            'display_name': display_name,       
        }

        result['users'].append(item)

    response = json.dumps(result)
    # logger.info("user_get_users")
    return Response(response=response, status=200, mimetype='application/json')


@app.route("/users/<user_id>",methods=["DELETE"])
def delete_user(user_id):

    # logger.info("user_deleted")
    
    cursor, conn = get_cursor()
    
    try:
        cursor.execute(f"""DELETE FROM main.users WHERE id = '{user_id}';""")
        conn.commit()
        print(records)
    except Exception as error:
        print(error)
    
    return Response(response=None, status=204, mimetype='application/json')


@app.route("/users/<user_id>",methods=["PATCH"])
def update_user(user_id):

    cursor, conn = get_cursor()
    request_data = request.get_json()

    try:
        cursor.execute(f"""
        UPDATE main.users
        SET display_name = '{request_data['display_name']}', login = '{request_data['login']}', hash = '{request_data['password']}'
        WHERE id = '{user_id}';
        """)
        conn.commit()
    except Exception as error:
        print(error)
        return Response(response=None, status=404, mimetype='application/json')

    

    return Response(response=None, status=204, mimetype='application/json')



if __name__ == '__main__':
    # hp_inf = get_config().get("web")
    # app.run(host=hp_inf.get("host"), port=hp_inf.get("port"))
    app.run(host="127.0.0.1", port=8888)