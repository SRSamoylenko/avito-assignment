FROM python:latest

WORKDIR /app

ENV PORT 8000

RUN pip install fastapi uvicorn[standard] psycopg2 sqlalchemy python-multipart

COPY ./app /app

CMD ["uvicorn", "main:app"]
