# database_setup.py
from app import app
from models import db, LotteryDraw

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'


with app.app_context():
    db.create_all()

    initial_data = [
        {"date": "January 2023", "draw1": 11, "draw2": 81, "draw3": 99},
        {"date": "February 2023", "draw1": 17, "draw2": 78, "draw3": 70},
        {"date": "March 2023", "draw1": 37, "draw2": 9, "draw3": 85},
        {"date": "April 2023", "draw1": 48, "draw2": 78, "draw3": 86},
        {"date": "May 2023", "draw1": 75, "draw2": 2, "draw3": 45},
        {"date": "June 2023", "draw1": 57, "draw2": 67, "draw3": 94},
        {"date": "July 2023", "draw1": 38, "draw2": 87, "draw3": 28},
        {"date": "August 2023", "draw1": 25, "draw2": 80, "draw3": 52},
        {"date": "September 2023", "draw1": 35, "draw2": 55, "draw3": 92},
        {"date": "October 2023", "draw1": 75, "draw2": 84, "draw3": 10},
        {"date": "November 2023", "draw1": 46, "draw2": 40, "draw3": 38},
        {"date": "December 2023", "draw1": 42, "draw2": 73, "draw3": 73},
        {"date": "January 2024", "draw1": 74, "draw2": 59, "draw3": 75},
        {"date": "February 2024", "draw1": 41, "draw2": 17, "draw3": 4},
        {"date": "March 2024", "draw1": 52, "draw2": 57, "draw3": 76},
        {"date": "April 2024", "draw1": 65, "draw2": 94, "draw3": 28},
        {"date": "May 2024", "draw1": 66, "draw2": 33, "draw3": 37},
        # Add the rest of your data here
    ]

    for data in initial_data:
        new_draw = LotteryDraw(date=data['date'], draw1=data['draw1'], draw2=data['draw2'], draw3=data['draw3'])
        db.session.add(new_draw)

    db.session.commit()
