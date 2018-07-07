import sqlite3
from datetime import datetime
from db.db import DB
from db.singleton import Singleton

class Sqlite3(DB):
  __metaclass__ = Singleton
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

    items = self._cursor.fetchone()
    return {
      "site": items[0],
      "title": items[1],
      "link": items[2],
      "date": items[3]
    }

