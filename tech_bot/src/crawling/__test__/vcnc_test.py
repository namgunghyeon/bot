import unittest
from src.crawling.vcnc import Vcnc
from db.bot_db import BotDB

class vcnc_test_case(unittest.TestCase):
  def setUp(self):
    self.vcnc = Vcnc(BotDB(db_name="sqlite3"))

  def test_fetch_latest_post(self):
    posts = self.vcnc._fetch_latest_post()

    self.assertEqual(True, len(posts) > 0)

    for post in posts:
      keys = post.keys()
      self.assertEqual((["site", "title", "link"]), list(keys))

  def test_get_latest_post_from_db(self):
    latest = self.vcnc._get_latest_post_from_db()

    keys = latest.keys()
    self.assertEqual((["site", "title", "link"]), list(keys))