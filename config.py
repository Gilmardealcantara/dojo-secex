import os


class ProjectPath(str):

    def __init__(self):
        self._project_path = os.getcwd()

    def __add__(self, path):
        self._project_path = os.path.join(self._project_path, path)
        return self

    def __radd__(self, text):
        self._project_path = text + self._project_path
        return self

    def __str__(self):
        return self._project_path
    
    def __repr__(self):
        return self._project_path

project_path = ProjectPath()

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + project_path + 'develop.db'


class Testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
