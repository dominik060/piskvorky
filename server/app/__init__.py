from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from hashlib import sha512

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database.db"
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.Text, primary_key = True)
    password_hash = db.Column(db.Text, nullable = False)

db.create_all()

@app.route("/account/<username>", methods=["POST"])
def account_post(username: str):
    password_hash = sha512(request.data).hexdigest()
    user = User(username=username, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return ""

@app.route("/account/<username>", methods=["DELETE"])
def account_delete(username: str):
    User.query.filter_by(username=username).delete()
    db.session.commit()
    return ""
