FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 21099

CMD ["sh", "-c", "python -m src.db_init && flask run"]
