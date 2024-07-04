# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from models import db, LotteryDraw

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/add_draw', methods=['POST'])
def add_draw():
    data = request.get_json()
    new_draw = LotteryDraw(date=data['date'], draw1=data['draw1'], draw2=data['draw2'], draw3=data['draw3'])
    db.session.add(new_draw)
    db.session.commit()
    return jsonify({'message': 'Draw added successfully'}), 201

@app.route('/predict', methods=['GET'])
def predict():
    draws = LotteryDraw.query.all()
    data = [[d.draw1, d.draw2, d.draw3] for d in draws]

    df = pd.DataFrame(data)
    lottery_data = df.values.flatten()

    X = []
    y = []

    n_lags = 10

    for i in range(n_lags, len(lottery_data)):
        X.append(lottery_data[i - n_lags:i])
        y.append(lottery_data[i])

    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    last_values = lottery_data[-n_lags:]

    predictions = []

    for _ in range(10):
        prediction = model.predict([last_values])[0]
        predictions.append(prediction)
        last_values = np.append(last_values[1:], prediction)

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
