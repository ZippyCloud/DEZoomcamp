#!/usr/bin/env python
# coding: utf-8

import argparse, os, sys
from time import time
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table
    url = params.url

    # Get the name of the file from url
    file_name = url.rsplit('/', 1)[-1].strip()
    print(f'Downloading {file_name} ...')
    # Download file from url
    os.system(f'wget {url.strip()} -O {file_name}')
    print('\n')

    # Create SQL engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # Read file based on csv or parquet
    if '.csv' in file_name:
        df = pd.read_csv(file_name, nrows=10)
        df_iter = pd.read_csv(file_name, iterator=True, chunksize=100000)
    elif '.parquet' in file_name:
        file = pq.ParquetFile(file_name)
        df = next(file.iter_batches(batch_size=10)).to_pandas()
        df_iter = file.iter_batches(batch_size=100000)
    else:
        print('Error. Only .csv or .parquet files allowed.')
        sys.exit()

    # Create the table
    df.head(0).to_sql(name=table, con=engine, if_exists='replace')

    # Insert values
    t_start = time()
    count = 0
    for batch in df_iter:
        count += 1
        if '.parquet' in file_name:
            batch_df = batch.to_pandas()
        else:
            batch_df = batch
        print(f'inserting batch {count}...')
        b_start = time()
        batch_df.to_sql(name=table, con=engine, if_exists='append')
        b_end = time()
        print(f'inserted! time taken {b_end - b_start:10.3f} seconds.\n')

    t_end = time()
    print(f'Completed! Total time taken was {t_end - t_start:10.3f} seconds for {count} batches.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data into a PostgreSQL database")
    parser.add_argument("--user", type=str, help="the user to connect to the database")
    parser.add_argument("--password", type=str, help="the password to connect to the database")
    parser.add_argument("--host", type=str, help="the host of the database")
    parser.add_argument("--port", type=int, help="the port of the database")
    parser.add_argument("--database", type=str, help="the database to connect to")
    parser.add_argument("--table", type=str, help="the table to insert the data into")
    parser.add_argument("--url", type=str, help="the URL of the CSV file to ingest")
    args = parser.parse_args()

    main(args)
