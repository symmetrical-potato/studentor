from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import LoginFormStudent


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login_student', methods=['GET', 'POST'])
def login():
    form = LoginFormStudent()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login_student.html',  title='Sign In', form=form)