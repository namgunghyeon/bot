import requests
import feedparser
from src.crawling.crawler import Crawler
from bs4 import BeautifulSoup

class Vcnc(Crawler):
  def __init__(self, db):
    self._web_base_url = "http://engineering.vcnc.co.kr/"
    self._feed_base_url = "http://engineering.vcnc.co.kr/atom.xml"
    self._bot_db = db

  def crawling(self):
    return self._fetch_latest_post()

  def get_new_post_and_update(self):
    posts = self.crawling()
    print (posts)
    last_post = self._get_latest_post_from_db()
    print (last_post)

    if len(posts) > 0:
      new_post = posts[0]

      if (new_post["title"] != last_post["title"]) and \
        (new_post["link"] != last_post["link"]):
        self._bot_db.save("vcnc", new_post["title"], new_post["link"])

        return new_post

    return None

  def _fetch_latest_post(self):
    feed = feedparser.parse(self._feed_base_url)

    posts = []
    for post in feed.entries:
      posts.append({
        'site': 'vcnc',
        'title': post.title,
        'link': post.link
      })

    return posts

  def _get_latest_post_from_db(self):
    latest_post = self._bot_db.get("vcnc")
    new_latest_post = {
      'site': 'vcnc',
      'title': '',
      'link': ''
    }

    if latest_post != None:
      new_latest_post['title'] = latest_post['title']
      new_latest_post['link'] = latest_post['link']


    return new_latest_post

  def web_crawling(self):
    response = requests.get(self._web_base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for link_tag in soup.select("link"):
      title = link_tag.get("title")
      href = link_tag.get("href")

      if title != None and title:
        links.append({
          'site': 'vcnc',
          'title': title,
          'href': href
        })

    for link in links:
      print(link)
