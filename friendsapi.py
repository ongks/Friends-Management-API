from flask import Flask, request


app = Flask(__name__)

@app.route('/api/v0/addfriendrequest', methods=['GET', 'POST'])
def add_friend_request():
    json_req = request.json
    return 'Hello World!'

if __name__ == '__main__':
    app.run()