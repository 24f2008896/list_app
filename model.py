from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many between Users and Lists
Users_Lists = db.Table('users_lists',
    db.Column('list_id', db.Integer, db.ForeignKey('lists.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    lists = db.relationship('Lists', secondary=Users_Lists, backref=db.backref('users'))

class Lists(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_name = db.Column(db.String, nullable=False)
    list_description = db.Column(db.String)
    # One-to-many relationship to List_Content - no secondary needed
    content = db.relationship('List_Content', backref='list')

class List_Content(db.Model):
    __tablename__ = 'list_content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key needed
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)  # fixed ForeignKey usage
    content = db.Column(db.String)
