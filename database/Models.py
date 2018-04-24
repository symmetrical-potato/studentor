import elasticsearch as esearch

from app import db, login
from flask_login import UserMixin
from flask import request

es = esearch.Elasticsearch()

@login.user_loader
def load_user(id):
    if request.cookies.get("role") == "student":
        return Student.query.get(int(id))
    else:
        return Employer.query.get(int(id))


class User:
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


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
    event_id = db.Column('event_id', db.String(120))
    checked = db.Column('checked', db.Boolean, default=False)


class Event:
    def __init__(self, name, description, diploma, employer_id, id=None):
        self.name = name
        self.description = description
        self.diploma = diploma
        self.employer_id = employer_id
        self.id = id

    def create(self):
        content = self.get_content()
        result = es.index(index='events', doc_type="event", body=content)
        self.id = result["_id"]

    def get_content(self):
        content = dict()

        content['name'] = self.name
        content['description'] = self.description
        content['employer_id'] = self.employer_id
        content['diploma'] = self.diploma
        if self.id is not None:
            content["_id"] = self.id

        return content

    @classmethod
    def get_by_id(cls, id):
        query = \
            {
                "query": {
                    "terms": {
                        "_id": id
                    }
                }
            }

        cur = es.search(index='uni', body=query)
        hit = list(cur['hits']['hits'])[0]
        document = hit['_source']

        return Event(document["name"], document["description"], document["diploma"],
                     document["employer_id"], id)

    @classmethod
    def get_by_employer(cls, employer_id):
        query = \
            {
                "query": {
                    "constant_score": {
                        "filter": {
                            "term": {
                                "employer_id": employer_id
                            }
                        }
                    }
                }
            }

        cur = es.search(index='events', body=query)
        result = []
        for hit in cur['hits']['hits']:
            document = hit['_source']
            result.append(Event(document["name"],
                                document["description"],
                                document["diploma"],
                                document["employer_id"],
                                id))
        return result


class Document:
    def __init__(self, filename, link, supervisor, text, title, type, university, year,
                 student_id, id=None):
        self.filename = filename
        self.link = link
        self.supervisor = supervisor
        self.text = text
        self.title = title
        self.type = type
        self.university = university
        self.year = year
        self.student_id = student_id
        self.id = id

    def get_content(self):
        content = dict(self.__dict__)

        if content["id"] is None:
            del content["id"]

        return content

    def create(self):
        content = self.get_content()
        result = es.index(index='documents', doc_type="document", body=content)
        self.id = result["_id"]

    @classmethod
    def get_by_id(cls, id):
        query = \
            {
                "query": {
                    "terms": {
                        "_id": id
                    }
                }
            }

        cur = es.search(index='documents', body=query)
        hit = list(cur['hits']['hits'])[0]
        document = hit['_source']

        return Document(**document)

    @classmethod
    def get_by_student(cls, student_id):
        query = \
            {
                "query": {
                    "constant_score": {
                        "filter": {
                            "term": {
                                "student_id": student_id
                            }
                        }
                    }
                }
            }

        cur = es.search(index='documents', body=query)
        result = []
        for hit in cur['hits']['hits']:
            document = hit['_source']
            result.append(Document(**document))
        return result

