from flask import Flask, request
from flask import render_template
import random

app = Flask(__name__)
sum = 0

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/random")                       # index.html에서 이 주소를 접속하여 해당 함수를 실행
def random_num():
    try:
        rand = random.randrange(1, 5001)
        global sum
        sum += rand
        return "ok"                         # 함수가 'ok'문자열을 반환함
    except :
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0")