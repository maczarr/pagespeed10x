FROM python:3.9-alpine
COPY crontab /etc/cron/crontab
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
WORKDIR /code
COPY . .
RUN crontab /etc/cron/crontab
CMD ["crond", "-f"]
