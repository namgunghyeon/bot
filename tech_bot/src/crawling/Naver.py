import requests
import feedparser
from src.crawling.Crawler import Crawler
from bs4 import BeautifulSoup

class Naver(Crawler):
  def __init__(self):
    self._web_base_url = "https://d2.naver.com/home"
    self._feed_base_url = "http://d2.naver.com/d2.atom"

  def crawling(self):
    return self._fetch_latest_post()

  def get_new_post(self):
    posts = self.crawling()
    last_post = self._get_latest_post_from_db()

    if len(posts) > 0:
      new_post = posts[0]

      if (new_post["title"] != last_post["title"]) and \
        (new_post["link"] != last_post["link"]):
        return new_post

    return None

  def _fetch_latest_post(self):
    feed = feedparser.parse(self._feed_base_url)

    posts = []
    for post in feed.entries:
      posts.append({
        'title': post.title,
        'link': post.link
      })

    return posts

  def _get_latest_post_from_db(self):
    return {
      'title': 'title',
      'link': 'link'
    }