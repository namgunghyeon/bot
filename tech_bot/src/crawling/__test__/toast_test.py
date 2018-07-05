import unittest
from src.crawling.toast import Toast

class toast_test_case(unittest.TestCase):
  def setUp(self):
    self.toast = Toast()

  def test_fetch_latest_post(self):
    posts = self.toast._fetch_latest_post()

    self.assertEqual(True, len(posts) > 0)

    for post in posts:
      keys = post.keys()
      self.assertEqual((["site", "title", "link"]), list(keys))

  def test_get_latest_post_from_db(self):
    latest = self.toast._get_latest_post_from_db()

    keys = latest.keys()
    self.assertEqual((["site", "title", "link"]), list(keys))