
FROM python:3.11-slim AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY requirements/production.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements/production.txt

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
