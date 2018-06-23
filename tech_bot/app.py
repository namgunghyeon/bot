from src.crawling.Baemin import Baemin
from src.crawling.Naver import Naver
from src.crawling.Kakao import Kakao
from src.crawling.Outsider import Outsider
from src.crawling.Medium import Medium

from slack.Slack import slack_notify

if __name__ == "__main__":
    baemin = Baemin()
    baemin.get_new_post()

    naver = Naver()
    naver.get_new_post()

    kakao = Kakao()
    kakao.get_new_post()

    outsider = Outsider()
    outsider.get_new_post()

    medium = Medium()
    medium.crawling()