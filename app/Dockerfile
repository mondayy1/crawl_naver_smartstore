FROM python:3.11-slim

RUN pip install --no-cache-dir poetry

COPY crawler ./app/source
COPY pyproject.toml poetry.lock* ./app/

WORKDIR app
RUN poetry self add poetry-plugin-shell \
    && poetry install