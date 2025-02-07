#!/usr/bin/env python
# coding: utf-8

import argparse, os, sys
import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time

def get_file_name(url: str):
    """Extract the file name from the URL"""
    return url.rsplit('/', 1)[-1].strip()

def download_file(url: str, file_name: str):
    """Download the file from specified URL"""
    print(f"Downloading {file_name}...")
    os.system(f"wget {url} -O {file_name}")
    print("Download complete!\n")


def postgres_engine(user: str, password: str, host: str, port: str, database: str):
    """Create a connection engine to the postgresql database"""
    print("Creating database connection...")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    print("Connection established!\n")
    return engine


def ingest_data(user: str, password: str, host: str, port: str, database: str, table: str, file_name: str):
    """Ingest data from a file to a database table"""
    engine = postgres_engine(user, password, host, port, database)

    if ".csv" in file_name:
        df = pd.read_csv(file_name, nrows=10)
        df_iterator = pd.read_csv(file_name, iterator=True, chunksize=100000)
    elif ".parquet" in file_name:
        file = pq.ParquetFile(file_name)
        df = next(file.iter_batches(batch_size=10)).to_pandas()
        df_iterator = file.iter_batches(batch_size=100000)
    else:
        print("Error: Only .csv or .parquet files are allowed.")
        sys.exit()

    print("\n\nStarting data ingestion...\n")
    df.head(0).to_sql(name=table, con=engine, if_exists="append")
    start_time = time()
    batch_count = 0
    for batch in df_iterator:
        batch_count += 1
        batch_df = batch.to_pandas() if file_name.endswith(".parquet") else batch
        print(f"Inserting batch {batch_count}...")
        batch_start = time()
        batch_df.to_sql(name=table, con=engine, if_exists='append')
        batch_end = time()
        print(f"Batch {batch_count} inserted! Time taken: {batch_end - batch_start:.3f} seconds.\n")
    end_time = time()
    print(f"Data ingestion completed! Total time: {end_time - start_time:.3f} seconds for {batch_count} batches.")


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table
    url = params.url
    file_name = get_file_name(url)

    download_file(url, file_name)
    ingest_data(user, password, host, port, database, table, file_name)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest data to a database')
    parser.add_argument('--user', type=str, help='Database username', default="kestra")
    parser.add_argument('--password', type=str, help='Database password', default="k3str4")
    parser.add_argument('--host', type=str, help='Database host', default="postgres")
    parser.add_argument('--port', type=int, help='Database port', default=5432)
    parser.add_argument('--database', type=str, help='Database name', default="postgres")
    parser.add_argument('--table', type=str, help='Table name')
    parser.add_argument('--url', type=str, help='URL of the file to ingest')
    args = parser.parse_args()
    main(args)