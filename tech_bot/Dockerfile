FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:fkrull/deadsnakes
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3.6 python3.6-dev python3-pip python3-setuptools python3-wheel gcc

RUN python3.6 -m pip install pip --upgrade

ADD . /bot-app

WORKDIR /bot-app

RUN pip3 install -r requirements.txt

CMD python3.6 app.py