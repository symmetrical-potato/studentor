from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    login = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Student {}>'.format(self.name)

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    login = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Employer {}>'.format(self.name)



'''

class Student(UserMixin, db.Model):
    name = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(255)) #hash
    avatar_hash = db.Column(db.String(255)) #default='2183364644805e13920dc9aff277f44f' hash картошки
    cv_hash = db.Column(db.String(255)) #hash
    university = db.Column(db.String(255))
    department = db.Column(db.String(255))

    def __repr__(self):
        return '<Student {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        return ''


@login.student_loader
def load_student(id):
    return Student.query.get(int(id))


class Employer(UserMixin, db.Model):
    name = db.Column('name', db.String(255), nullable=False)
    login = db.Column('login', db.String(255))
    password = db.Column('password', db.String(255))  # hash
    avatar = db.Column('avatar', db.String(255))  # default='2183364644805e13920dc9aff277f44f' hash картошки
    contacts = db.Column('contacts', db.String(255))
    description = db.Column('description', db.String(1500))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        return ''


@login.employer_loader
def load_employer(id):
    return Employer.query.get(int(id))


class Event(BaseModel):
    
    __tablename__ = 'events'
    name = db.Column('name', db.String(255))
    description = db.Column('description', db.String(1500))
    diploma = db.Column('diploma', Boolean) #true - если тема диплома, false - усли стажировка
    employer_id = db.Column('employer_id', Integer, ForeignKey('employers.id'))

    employer = relationship(Employer)



class Document(BaseModel):
    __tablename__ = 'documents'
    filename = db.Column('filename', db.String(255))
    link = db.Column('link', db.String(255))
    supervisor = db.Column('supervisor', db.String(255))
    text = db.Column('text', db.String(1000000))
    title = db.Column('title', db.String(500))
    type = db.Column('type', db.String(500))
    university = db.Column('description', db.String(255))
    year = db.Column('year', Integer)
    student_id = db.Column('student_id', Integer, ForeignKey('students.id'))

    student = relationship(Student)

'''