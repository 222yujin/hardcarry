from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


client = MongoClient('mongodb://test:test@localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.catchup


@app.route('/')
def home():
    return render_template('index.html')


# get method
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"isSuccess": "success", "test": "get test"})


# post method
@app.route('/eroomy', methods=['POST'])
def post():
    # request 받아서 내부처리
    # 결과 response로 반환
    name_receive = request.form['name']
    phone_receive = request.form['phone']

    db.eroomy.insert_one({"name": name_receive, "phone": phone_receive})

    return jsonify({"isSuccess": True, "test": "데이터 저장 성공"})


#################################################################

# get method
@app.route('/app/auth', methods=['GET'])
def get_auth():
    # 내부 동작

    return jsonify({"isSuccess": True, "code": 1000, "message": "요청에 성공하였습니다."
                       , "result": {"accountId": 1, "nickname": "test", "participationCount": 1, "profileImage": None,
                                    "address": "서울특별시 사당로 20나길"}})


# post method
@app.route('/app/sign-up', methods=['POST'])
def sign_up():
    email_receive = request.form['email']
    nickname_receive = request.form['nickname']
    password_receive = request.form['password']
    address_receive = request.form['address']

    # request 받아서 내부처리
    # 결과 response로 반환

    return jsonify({"isSuccess": True, "code": 1000, "message": "요청에 성공하였습니다.",
                    "result": {"accountId": 2, "nickname": "vividswan", "address": "서울특별시 사당로 20나길 19 201호"}})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
