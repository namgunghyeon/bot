from src.crawling.baemin import Baemin
from src.crawling.naver import Naver
from src.crawling.kakao import Kakao
from src.crawling.outsider import Outsider
from src.crawling.medium import Medium
from db.bot_db import BotDB

from slack.slack import slack_notify

if __name__ == "__main__":

    baemin = Baemin()
    baemin.get_new_post_and_update()

    naver = Naver()
    naver.get_new_post()

    kakao = Kakao()
    kakao.get_new_post()

    outsider = Outsider()
    outsider.get_new_post()

    medium = Medium()
    medium.crawling()