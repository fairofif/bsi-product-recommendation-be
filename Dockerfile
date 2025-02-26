ARG PYTHON_VERSION=3.11.6
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

USER appuser

COPY . .

EXPOSE 21099

CMD ["sh", "-c", "python -m src.db_init && gunicorn -b 0.0.0.0:21099 'src.app:app'"]

# FROM python:3.10

# WORKDIR /app

# RUN pip install --upgrade pip

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 21099

# CMD ["sh", "-c", "python -m src.db_init && flask run"]
