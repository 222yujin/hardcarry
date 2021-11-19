from flask import Flask, render_template, jsonify, request
import json
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://test:test@13.125.132.62', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.catchup


@app.route('/')
def home():
    return render_template('index.html')


# test 점수 계산해서 결과 주기
@app.route('/result', methods=['GET'])
def test_result_get():
    result_score = request.args.get('result_array')
    result_score = result_score.split('_')

    result_type = 1
    if (result_score[0] == '0' and result_score[1] == '1') or (result_score[1] == '1' and result_score[2] == '1') or (
            result_score[0] == '0' and result_score[2] == '1'):
        result_type = 2

    if result_score[3] == '0' or (result_score[4] == '0' and result_score[5] == '0'):
        result_type = 3

    if result_score[6] == '0' or (result_score[7] == '1' and result_score[8] == '0') or result_score[11] == '1':
        result_type = 4


    category = db.category.find_one({"type": result_type}, {"_id": False})
    category["programs"] = []
    for i in category["id"]:
        category["programs"].append(db.program.find_one({"id": i}, {"_id": False}))
    print(category)
    return jsonify({"isSuccess": "success", "data": category})


# post 사용 x
@app.route('/result', methods=['POST'])
def test_result():
    result_score = request.form.get('result_array')
    print(result_score)
    result_score = result_score.split('_')
    print(result_score)
    result_type = 0

    if result_score[3] == '1' or (result_score[4] == '1' and result_score[5] == '1'):
        result_type = 2
        if result_score[6] == '1' or (result_score[7] == '1' and result_score[8] == '1'):
            result_type = 3
            if result_score[9] == '1' or (result_score[10] == '1' and result_score[11] == '1'):
                result_type = 4
    else:
        result_type = 1

    category = db.category.find_one({"type": result_type}, {"_id": False})
    category["programs"] = []
    for i in category["id"]:
        category["programs"].append(db.program.find_one({"id": i}, {"_id": False}))
    print(category)
    return jsonify({"isSuccess": "success", "data": category})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
