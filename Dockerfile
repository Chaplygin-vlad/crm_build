
FROM python:3.9
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV \
  # poetry:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'
WORKDIR /app/crm
RUN apt-get update && \
    pip install --upgrade pip poetry
COPY poetry.lock pyproject.toml /app/crm/
RUN poetry install --no-interaction --no-ansi && \
	rm -rf "$POETRY_CACHE_DIR"

COPY crm .
RUN mkdir staticdir