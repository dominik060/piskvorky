from click import password_option
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


@app.route("/account/<username>/exists")
def account_exists(username: str):
    if User.query.filter_by(username=username).count() != 0:
        return ""
    else:
        return ("User doesn't exists", 404)


@app.route("/validate-credentials")
def alidate_credentials():
    username = request.authorization["username"]
    password_hash = sha512(request.authorization["password"].encode("utf-8")).hexdigest()

    if User.query.filter_by(username=username, password_hash=password_hash).count() != 0:
        return ""
    else:
        return ("Invalid credentials", 400)


@app.route("/account/<username>", methods=["POST"])
def account_post(username: str):
    password_hash = sha512(request.data).hexdigest()
    user = User(username=username, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return ""

@app.route("/account/<username>", methods=["DELETE"])
def account_delete(username: str):
    if username != request.authorization["username"]: 
        return ("Cannot delete other user", 403)

    password_hash = sha512(request.authorization["password"].encode("utf-8")).hexdigest()

    if User.query.filter_by(username=username, password_hash=password_hash).delete() == 0:
        return("Wrong credentials", 401)

    db.session.commit()
    return ""


"""@app.route("/test")
def test():
    username = request.authorization["username"]
    password = request.authorization["password"]
    password_hash = sha512(password).hexdigest()
    try:
        User.query.filter_by(username=username, password_hash=password_hash).delete()
        return f"User: {username} was deleted successfully"
    except:
        return f"No existing user: {username} with password: {password}"
   #return f"Provided user: {username} with password: {password}
   """
