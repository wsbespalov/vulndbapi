import os
from datetime import datetime
from sqlalchemy import create_engine, exists, Column, DateTime, Integer, String, MetaData, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Vulnerability

basedir = os.path.abspath(os.path.dirname(__file__))

metadata = MetaData()
engine = create_engine('sqlite:///' + os.path.join(basedir, 'stats.db'), echo=False)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class DBHelper(object):

    def __init__(self):
        pass

    def insert(self, data):
        pass

    def exists(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, data):
        pass
