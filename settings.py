from database.Models import Student, Document, Employer, Event

LOCAL_DB = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'Lm14vZ',
    'database': 'studentor'
}

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgres://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s' \
                          % LOCAL_DB
SQLALCHEMY_TRACK_MODIFICATIONS = True

URL_PREFIX = 'api'
HATEOAS = False
IF_MATCH = False