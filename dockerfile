FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update -y && apt-get install gcc libc-dev -y

RUN pip install -r /requirements.txt
RUN pip install gunicorn

RUN mkdir /app
WORKDIR /app
COPY . /app

CMD python manage.py migrate && gunicorn app.wsgi --bind 0.0.0.0:80 --workers 1
