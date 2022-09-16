from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

data = {
    "903bc01c08171cc1538532c73a4a353cf1a71ebc": {
        "display_name": "cop"
    }
}

@app.route('/users',methods=["POST"])
def create_user():
    request_data = request.get_json()
    print(request_data)
    id = str(uuid4())
    new_user = {
        id: {
            "display_name": request_data.get("display_name")
        }
    }
    data.update(new_user)
    print(data)
    return {"success": True}

'''
@app.route('/users/<user_id>',methods=["GET"])
def get_user():
    return jsonify({
        "id": id,
        request
    })
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)