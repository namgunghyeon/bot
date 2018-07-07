import sqlite3
from datetime import datetime
from db.sqlite3 import Sqlite3
from db.dynamo_db import DynamoDB
from db.singleton import Singleton

class BotDB():
  __metaclass__ = Singleton
  def __init__(self, db_name):
    self._db_name = db_name

    if (self._db_name == "sqlite3"):
      self._db = Sqlite3()

    elif (self._db_name == "dynamo_db"):
      self._db = DynamoDB()

    else:
      raise ValueError('Invalid db name')

  def save(self, site, title, link):
    self._db.save(site, title, link)

  def get(self, site):
    return self._db.get(site)
