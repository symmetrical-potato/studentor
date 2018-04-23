import os

from pathlib import Path


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOME = str(Path.home())
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://artyom:ilavah84@localhost/studentor?client_encoding' \
                              '=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DATA_LOADER_PERIOD = 10 #seconds

    VK_API_KEY = os.environ.get('VK_API_KEY')

    PATH_TO_CACHE_DIR = os.path.join(HOME, ".cache/studentor")
    PATH_TO_LOG_DIR = os.path.join(PATH_TO_CACHE_DIR, "log")
    
    PATH_TO_DATA_LOADER_CACHE = os.path.join(PATH_TO_CACHE_DIR, "data_loader_cache.txt")
    PATH_TO_DATA_LOADER_LOG = os.path.join(PATH_TO_LOG_DIR, "data_loader_log.txt")
    UPLOAD_FOLDER = os.path.join(PATH_TO_CACHE_DIR, 'diplomas')

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.PATH_TO_CACHE_DIR, exist_ok=True)
os.makedirs(Config.PATH_TO_LOG_DIR, exist_ok=True)