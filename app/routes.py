from flask import render_template, redirect, url_for, flash
from app import app


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/stud/login')
def stud_login():
    return render_template('login.html', page_title="Student Login")

@app.route('/stud/signup')
def stud_signup():
    return render_template('signup.html', page_title="Student Sign Up")

@app.route('/empl/login')
def empl_login():
    return render_template('login.html', page_title="Employer Login")

@app.route('/empl/signup')
def empl_signup():
    return render_template('signup.html', page_title="Employer Sign Up")

@app.route('/stud/test')
def test_user_profile():
    return render_template('student.html', diplomas = [
        ("Тема диплома №1", "Описание диплома №1", "Данные диплома №1", "Еще что-то диплома №1"),
        ("Тема диплома №2", "Описание диплома №2", "Данные диплома №2", "Еще что-то диплома №2"),
        ("Тема диплома №3", "Описание диплома №3", "Данные диплома №3", "Еще что-то диплома №3")
    ])