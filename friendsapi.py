from flask import Flask, request, jsonify
from jsonschema import ValidationError
from data import friends, block, get_updates
import schemas, managefriends


app = Flask(__name__)

@app.route('/api/v0/addfriendrequest', methods=['GET', 'POST'])
def add_friend():
    json_req = request.json
    try:
        schemas.validate_friends_pair(json_req)
        json_resp = managefriends.add_friend_request(json_req, friends, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/listfriends', methods=['GET', 'POST'])
def list_friends():
    json_req = request.json
    try:
        schemas.validate_single_email(json_req)
        json_resp = managefriends.list_friends_request(json_req, friends)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/mutualfriends', methods=['GET', 'POST'])
def list_mutual_friends():
    json_req = request.json
    try:
        schemas.validate_friends_pair(json_req)
        json_resp = managefriends.list_mutual_friends_request(json_req, friends)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/subscribeupdates', methods=['GET', 'POST'])
def sub_updates():
    json_req = request.json
    try:
        schemas.validate_requestor_target(json_req)
        json_resp = managefriends.sub_updates_request(json_req, get_updates, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/BlockUpdates', methods=['GET', 'POST'])
def blockUpdates():
    json_req = request.json
    return 'Hello World!'

@app.route('/api/v0/ListUpdatedEmails', methods=['GET', 'POST'])
def listUpdatedEmails():
    json_req = request.json
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
