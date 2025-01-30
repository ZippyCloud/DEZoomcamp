FROM python:3.9

RUN apt-get update && apt-get install -y wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app

COPY ingest-data.py ingest-data.py

ENTRYPOINT ["python", "ingest-data.py"]