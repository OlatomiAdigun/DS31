from flask import Flask
from flask import render_template
from flask import request
from .models import  db, User
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))

def create_app():

    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def main():
        name = request.form.get("name")
        
        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        users = User.query.all()
        return render_template("home.html", users=users)

    @app.route('/about')
    def about():
        return 'This is the coolest app ever !!!'

    return app