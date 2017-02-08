FROM python:3.6
MAINTAINER Maxime Chéramy <maxime@codingame.com>
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
