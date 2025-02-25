
FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

RUN python -m src.db_init

EXPOSE 8000

CMD ["flask", "run"]
