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
RUN pip3 install pipenv

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONPATH /usr/src/udk

WORKDIR /usr/src/udk

COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --deploy --ignore-pipfile

ENV FLASK_APP=app/main.py
EXPOSE 5000
ADD . .

CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
