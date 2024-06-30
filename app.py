import time

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
db = SQLAlchemy(app)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    score = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    secs_since_epoch = db.Column(db.Float, default=time.time())
    computer_name = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    screen_width = db.Column(db.Integer, nullable=False)
    screen_height = db.Column(db.Integer, nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Server is running'}), 200


@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    ip_address = request.remote_addr
    new_score = Result(
        name=data['name'],
        nickname=data['nickname'],
        email=data['email'],
        score=float(data['score']),
        computer_name=data['computer_name'],
        os=data['os'],
        screen_width=data['screen_width'],
        screen_height=data['screen_height'],
        ip_address=ip_address
    )
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score submitted successfully!'})


@app.route('/get_scores', methods=['GET'])
def get_scores():
    scores = Result.query.order_by(Result.score.desc()).all()
    output = []
    for score in scores:
        score_data = {
            'name': score.name,
            'nickname': score.nickname,
            'email': score.email,
            'score': score.score,
            'date_time': score.date_time,
            'computer_name': score.computer_name,
            'os': score.os,
            'screen_width': score.screen_width,
            'screen_height': score.screen_height,
            'ip_address': score.ip_address
        }
        output.append(score_data)
    return jsonify(output)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8123, debug=True)
