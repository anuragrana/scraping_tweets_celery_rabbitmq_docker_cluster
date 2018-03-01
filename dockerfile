FROM python:3
ADD requirements.txt /app/requirements.txt
ADD ./celery_main/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A celery_main worker --concurrency=5 --loglevel=info

