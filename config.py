import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Lm14vZ@localhost/studentor?client_encoding' \
                              '=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DATA_LOADER_PERIOD = 10 #seconds

    VK_API_KEY = os.environ.get('VK_API_KEY')

    PATH_TO_CACHE_DIR = os.path.join(basedir, ".cache")
    PATH_TO_LOG_DIR = os.path.join(basedir, ".log")
    
    PATH_TO_DATA_LOADER_CACHE = os.path.join(PATH_TO_CACHE_DIR, "data_loader_cache.txt")
    PATH_TO_DATA_LOADER_LOG = os.path.join(PATH_TO_LOG_DIR, "data_loader_log.txt")
    UPLOAD_FOLDER = '/home/merlin/.cache/studentor/diplomas/'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.isdir(Config.PATH_TO_CACHE_DIR):
    os.mkdir(Config.PATH_TO_CACHE_DIR)

if not os.path.isdir(Config.PATH_TO_LOG_DIR):
    os.mkdir(Config.PATH_TO_LOG_DIR)