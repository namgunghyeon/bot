import unittest
from src.crawling.dramaandcompany import Dramancompany
from db.bot_db import BotDB

class dramaandcompany_test_case(unittest.TestCase):
  def setUp(self):
    self.dramaandcompany = Dramancompany(BotDB(db_name="sqlite3"))

  def test_fetch_latest_post(self):
    posts = self.dramaandcompany._fetch_latest_post()

    self.assertEqual(True, len(posts) > 0)

    for post in posts:
      keys = post.keys()
      self.assertEqual((["site", "title", "link"]), list(keys))

  def test_get_latest_post_from_db(self):
    latest = self.dramaandcompany._get_latest_post_from_db()

    keys = latest.keys()
    self.assertEqual((["site", "title", "link"]), list(keys))