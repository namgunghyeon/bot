import requests
import feedparser
from src.crawling.Crawler import Crawler
from bs4 import BeautifulSoup

class Outsider(Crawler):
  def __init__(self):
    self._web_base_url = "https://blog.outsider.ne.kr/?page=1"
    self._feed_base_url = "http://feeds2.feedburner.com/rss_outsider_dev"

  def crawling(self):
    feed = feedparser.parse(self._feed_base_url)

    links = []
    for post in feed.entries:
      links.append({
        'title': post.title,
        'href': post.link
      })

    for link in links:
      print(link)

  def web_crawling(self):
    response = requests.get(self._web_base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for link_tag in soup.select("link"):
      title = link_tag.get("title")
      href = link_tag.get("href")

      if title != None and title:
        links.append({
          'title': title,
          'href': href
        })

    for link in links:
      print(link)
