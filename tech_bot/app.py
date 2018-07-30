from src.crawling.baemin import Baemin
from src.crawling.naver import Naver
from src.crawling.kakao import Kakao
from src.crawling.outsider import Outsider
from src.crawling.vcnc import Vcnc
from src.crawling.toast import Toast
from db.bot_db import BotDB
from db.dynamo_db import DynamoDB
from slack.slack import slack_notify
from config import DBConfig

def build_slack_attachments(posts):
  attachments = {}
  attachments["pretext"] = ":mega: 기술 블로그 업데이트"
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
    message += """*{}* \n • {} \n   • {} \n""".format(site, title, link)

  return message

def send_posts(posts):
  if len(posts) > 0:
    attachments = build_slack_attachments(posts)
    slack_notify(channel="#it_news", attachments=[attachments])

def check():
  bot_db = BotDB(db_name=DBConfig.db_name)
  posts = []
  sites = [
    Baemin(db=bot_db),
    Naver(db=bot_db),
    Kakao(db=bot_db),
    Kakao(db=bot_db),
    Outsider(db=bot_db),
    Vcnc(db=bot_db)
  ]

  for crawler in sites:
    post = crawler.get_new_post_and_update()

    if (post != None):
      posts.append(post)

  send_posts(posts)

if __name__ == "__main__":
  check()