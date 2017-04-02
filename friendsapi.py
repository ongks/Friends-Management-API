from flask import Flask, request, jsonify
from jsonschema import ValidationError
from managefriends import add_friend_request, list_friends_request
from data import friends, block
import schemas


app = Flask(__name__)

@app.route('/api/v0/addfriendrequest', methods=['GET', 'POST'])
def add_friend_request():
    json_req = request.json
    try:
        schemas.validate_friends_pair(json_req)
        json_resp = add_friend_request(json_req, friends, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/listfriends', methods=['GET', 'POST'])
def list_friends():
    json_req = request.json
    try:
        schemas.validate_single_email(json_req)
        json_resp = list_friends_request(json_req, friends)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

if __name__ == '__main__':
    app.run()