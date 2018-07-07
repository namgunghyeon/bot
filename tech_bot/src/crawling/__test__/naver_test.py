import unittest
from src.crawling.naver import Naver
from db.bot_db import BotDB

class naver_test_case(unittest.TestCase):
  def setUp(self):
    self.naver = Naver(BotDB(db_name="sqlite3"))

  def test_fetch_latest_post(self):
    posts = self.naver._fetch_latest_post()

    self.assertEqual(True, len(posts) > 0)

    for post in posts:
      keys = post.keys()
      self.assertEqual((["site", "title", "link"]), list(keys))

  def test_get_latest_post_from_db(self):
    latest = self.naver._get_latest_post_from_db()

    keys = latest.keys()
    self.assertEqual((["site", "title", "link"]), list(keys))