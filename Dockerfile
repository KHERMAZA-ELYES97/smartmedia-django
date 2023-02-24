FROM python:3.9.0-alpine
WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --no-create-home app

COPY --chown=app:app ./requirements.txt /requirements.txt

RUN apk add --no-cache build-base linux-headers && \
	pip install --upgrade pip && \
    apk add --update --no-cache sqlite-dev && \
    apk add --update --no-cache --virtual .tmp-deps build-base musl-dev && \
	pip install -r /requirements.txt && \
    apk del build-base linux-headers

COPY --chown=app:app ./app /app

USER app
EXPOSE 8000

CMD sh -c "python manage.py makemigrations; \
	python manage.py migrate; \
	rm -r /app/static-dump/*; python manage.py collectstatic; \
	python manage.py createsuperuser --noinput --username smartmedia --email "ekhermaza@citc-eurarfid.com"; \
	uwsgi --http :8000 --workers 4 --master --enable-threads --module app.wsgi"
