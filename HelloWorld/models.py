from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creates a 'user' table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id as primary key
    name = db.Column(db.String(50), nullable=False) # user name

    def __repr__(self):
        return "<User: {}>".format(self.name)