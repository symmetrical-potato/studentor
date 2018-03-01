import json

from flask import render_template, redirect, url_for, flash, request, abort, make_response
from app import app
from database.Models import *
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/stud/login', methods=['GET', 'POST'])
def get_stud_login():
    if request.method == "GET":
        res = make_response(render_template('login.html', page_title="Student Login",
                                            action="stud"))
        res.set_cookie("role", "student")
        return res
    else:
        username = request.form.get('Username')
        password = request.form.get('Password')

        user = Student.query.filter_by(login=username).first()
        if user is None or not user.check_password(password):
            return json.dumps({'error': 'Неправильный логин или пароль!'})

        login_user(user)
    return json.dumps({'success': user.id})

@app.route('/stud/signup', methods=['GET', 'POST'])
def get_stud_signup():
    if request.method == 'GET':
        res = make_response(render_template('signup.html', page_title="Student Sign Up",
                                            action='stud'))
        res.set_cookie("role", "student")
        return res
    else:
        username = request.form.get('Username')
        password = request.form.get('Password')
        email = request.form.get('Email')

        user = Student.query.filter_by(login=username).first()
        if user is not None:
            return json.dumps({'error':'Пользователь с таким email уже существует.'})

        user = Student()
        user.name = username
        user.login = email
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return json.dumps({'success': user.id})


@app.route('/empl/login', methods=['GET', 'POST'])
def get_empl_login():
    if request.method == "GET":
        res = make_response(render_template('login.html', page_title="Employer Login",
                                            action="empl"))
        res.set_cookie("role", "employer")
        return res
    else:
        username = request.form.get('Username')
        password = request.form.get('Password')

        user = Employer.query.filter_by(login=username).first()
        if user is None or not user.check_password(password):
            return json.dumps({'error': 'Неправильный логин или пароль!'})

        login_user(user)
    return json.dumps({'success': user.id})

@app.route('/empl/signup', methods=['GET'])
def get_empl_signup():
    if request.method == 'GET':
        res = make_response(render_template('signup.html', page_title="Employer Sign Up",
                                            action='empl'))
        res.set_cookie("role", "employer")
        return res
    else:
        username = request.form.get('Username')
        password = request.form.get('Password')
        email = request.form.get('Email')

        user = Employer.query.filter_by(login=username).first()
        if user is not None:
            return json.dumps({'error':'Пользователь с таким email уже существует.'})

        user = Employer()
        user.name = username
        user.login = email
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return json.dumps({'success': user.id})


@app.route('/stud/test')
def test_user_profile():
    return render_template('student.html', diplomas = [
        ("Тема диплома №1", "Описание диплома №1", "Данные диплома №1", "Еще что-то диплома №1"),
        ("Тема диплома №2", "Описание диплома №2", "Данные диплома №2", "Еще что-то диплома №2"),
        ("Тема диплома №3", "Описание диплома №3", "Данные диплома №3", "Еще что-то диплома №3")
    ])

@app.route('/success')
@login_required
def success():
    return render_template('test.html')


@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for("index"))
