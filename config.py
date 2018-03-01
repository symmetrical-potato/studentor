import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Lm14vZ@212.109.223.117/studentor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False