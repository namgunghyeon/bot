import requests
import feedparser
from src.crawling.crawler import Crawler
from db.bot_db import BotDB
from bs4 import BeautifulSoup
from selenium import webdriver

class Toast(Crawler):
  def __init__(self):
    self._web_base_url = "http://meetup.toast.com"
    self._feed_base_url = "http://meetup.toast.com/"
    self._bot_db = BotDB()

  def crawling(self):
    return self._fetch_latest_post()

  def get_new_post_and_update(self):
    posts = self.crawling()
    last_post = self._get_latest_post_from_db()

    if len(posts) > 0:
      new_post = posts[0]

      if (new_post["title"] != last_post["title"]) and \
        (new_post["link"] != last_post["link"]):
        self._bot_db.save("toast", new_post["title"], new_post["link"])

        return new_post

    return None

  def _fetch_latest_post(self):
    return self.web_crawling()

  def _get_latest_post_from_db(self):
    latest_post = self._bot_db.get("toast")
    new_latest_post = {
      'site': 'toast',
      'title': '',
      'link': ''
    }

    if latest_post != None and len(latest_post) > 0:
      new_latest_post['title'] = latest_post[1]
      new_latest_post['link'] = latest_post[2]

    return new_latest_post

  def web_crawling(self):
    driver = webdriver.Chrome("lib/mac/chromedriver")
    driver.implicitly_wait(3)
    driver.get(self._web_base_url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    posts = []

    for box in soup.findAll("a", {"class": "lst_link"}):
      title = box.find("h3", {"class": "tit ng-binding"})
      href = box.get("href")

      if title != None and title:
        posts.append({
          'site': 'toast',
          'title': title.get_text(),
          'link': "{}{}".format(self._web_base_url, href)
        })

    return posts

