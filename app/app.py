from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template('student.html')

if __name__ == '__main__':
    app.run()
