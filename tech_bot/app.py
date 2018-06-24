from src.crawling.baemin import Baemin
from src.crawling.naver import Naver
from src.crawling.kakao import Kakao
from src.crawling.outsider import Outsider
from src.crawling.medium import Medium
from db.bot_db import BotDB
from slack.slack import slack_notify

from slack.slack import slack_notify

def build_slack_attachments(posts):
  attachments = {}
  attachments["pretext"] = "기술 블로그 업데이트"
  attachments["title"] = "내용"
  attachments["text"] = build_text(posts)
  attachments["mrkdwn_in"] = ["text"]

  return attachments

def build_text(posts):
  message = ""

  for post in posts:
    site = post['site']
    title = post['title']
    link = post['link']
    message += """*{}* \n {} \n {} \n""".format(site, title, link)

  return message

def send_posts(posts):
  attachments = build_slack_attachments(posts)

  slack_notify(channel="#it_news", attachments=[attachments])

if __name__ == "__main__":
  posts = []
  sites = [Baemin(), Naver(), Kakao(), Kakao(), Outsider()]

  for crawler in sites:
    post = crawler.get_new_post_and_update()

    if (post != None):
      posts.append(post)

  send_posts(posts)
