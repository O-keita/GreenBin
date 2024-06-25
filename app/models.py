from app import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    adress = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    img_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return '<User %r>' % self.name
    

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    collected = db.Column(db.Boolean, nullable=False, default=False)


    def __repr__(self):
        return '<Schedule %r>' % self.date