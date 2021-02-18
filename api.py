from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000/"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pi_db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

@app.route('/api/get_all_users/', methods=['GET'])
@cross_origin()
def get_all_users():

    all_users_db = Users.query.all()
    all_users = []

    for user in all_users_db:
        users_info = {}
        users_info['user_id'] = user.user_id
        users_info['first_name'] = user.first_name
        users_info['last_name'] = user.last_name
        all_users.append(users_info)
    print(all_users)

    return { 'all_users': all_users}
