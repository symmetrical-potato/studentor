from app import app, db
from database.Models import Student, Employer


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Student': Student, 'Employer': Employer}