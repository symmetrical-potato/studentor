from flask import render_template, redirect, url_for, flash, request
from app import app


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/stud/login', methods=['GET'])
def get_stud_login():
    return render_template('login.html', page_title="Student Login", action='stud')

@app.route('/stud/signup', methods=['GET'])
def get_stud_signup():
    return render_template('signup.html', page_title="Student Sign Up", action='stud')

@app.route('/stud/login', methods=['POST'])
def login_student():
    username = request.form.get('Username')
    password = request.form.get('Password')
    return str(username + " " + password)

@app.route('/empl/login', methods=['GET'])
def get_empl_login():
    return render_template('login.html', page_title="Employer Login", action='empl')

@app.route('/empl/signup', methods=['GET'])
def get_empl_signup():
    return render_template('signup.html', page_title="Employer Sign Up", action='empl')

@app.route('/empl/login', methods=['POST'])
def login_empl():
    username = request.form.get('Username')
    password = request.form.get('Password')
    return str(username + " " + password)

@app.route('/stud/test')
def test_user_profile():
    return render_template('student.html', diplomas = [
        ("Тема диплома №1", "Описание диплома №1", "Данные диплома №1", "Еще что-то диплома №1"),
        ("Тема диплома №2", "Описание диплома №2", "Данные диплома №2", "Еще что-то диплома №2"),
        ("Тема диплома №3", "Описание диплома №3", "Данные диплома №3", "Еще что-то диплома №3")
    ])