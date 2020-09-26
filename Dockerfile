FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 \
    python3-venv \
    python3-dev \
    libmysqlclient-dev \
    mysql-server \
    build-essential \
    python3-pip

RUN pip3 install --upgrade pip

WORKDIR /usr/src/app

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app/main.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

ADD . .
