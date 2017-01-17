FROM python:3.6
MAINTAINER Maxime Chéramy <maxime@codingame.com>
COPY tests.py /opt/
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
