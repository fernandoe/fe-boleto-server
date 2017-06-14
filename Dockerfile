FROM fernandoe/docker-python:0.0.4
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>

ENV http_proxy http://15.85.195.199:8088
ENV https_proxy http://15.85.195.199:8088
ENV HTTP_PROXY http://15.85.195.199:8088
ENV HTTPS_PROXY http://15.85.195.199:8088

RUN apt-get update && apt-get install -y \
  mongodb-clients \
  mysql-client \
  python3-pip

RUN apt-get -y autoremove
RUN apt-get -y autoclean
RUN apt-get -y clean

ADD ./requirements /requirements
ADD ./source /app

RUN pip3 install -r /requirements/docker.txt

CMD python3 manage.py runserver 0.0.0.0:8000

WORKDIR /app
