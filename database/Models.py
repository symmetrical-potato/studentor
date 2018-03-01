from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import request

@login.user_loader
def load_user(id):
    if request.cookies.get("role") == "student":
        return Student.query.get(int(id))
    else:
        return Employer.query.get(int(id))


class User():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    login = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(128))
    contacts = db.Column(db.String(500))

    def set_password(self, password):
        self.password_hash = password

    def check_password(self, password):
        return self.password_hash == password


class Student(UserMixin, User, db.Model):
    cv_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Student {}>'.format(self.name)

class Employer(UserMixin, User, db.Model):
    description = db.Column(db.String(1500))
    def __repr__(self):
        return '<Employer {}>'.format(self.name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(255))
    description = db.Column('description', db.String(1500))
    diploma = db.Column('diploma', db.Boolean)
    employer_id = db.Column('employer_id', db.Integer, db.ForeignKey('employer.id'))


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column('filename', db.String(255))
    link = db.Column('link', db.String(255))
    supervisor = db.Column('supervisor', db.String(255))
    text = db.Column('text', db.String(1000000))
    title = db.Column('title', db.String(500))
    type = db.Column('type', db.String(500))
    university = db.Column('description', db.String(255))
    year = db.Column('year', db.Integer)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.id'))


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
    event_id = db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
    checked = db.Column('checked', db.Boolean, default=False)

