import sqlite3
from datetime import datetime

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

class BotDB(metaclass=Singleton):
  def __init__(self):
    self._conn = sqlite3.connect("db/bot.db")
    self._cursor = self._conn.cursor()

    self._init_table()

  def _init_table(self):
    self._cursor.execute("""
      CREATE TABLE IF NOT EXISTS `crawling`(
        `site` TEXT NOT NULL,
        `title` TEXT NOT NULL,
        `link` TEXT NOT NULL,
        'date' DATETIME,
        PRIMARY KEY(`site`)
      )
    """)
    self._conn.commit()

  def save(self, site, title, link):
    self._cursor.execute("""
      INSERT OR REPLACE INTO crawling(
        `site`,
        `title`,
        `link`,
        `date`
      ) VALUES (
        "{}",
        "{}",
        "{}",
        "{}"
      )
    """.format(site, title, link, datetime.now()))

    self._conn.commit()

  def get(self, site):
    self._cursor.execute(
      """
        SELECT
          `site`,
          `title`,
          `link`,
          `date`
        FROM
          crawling
        WHERE
          site = "{}"
      """.format(site)
    )

    return self._cursor.fetchone()
