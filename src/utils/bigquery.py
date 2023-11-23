import os
from datetime import datetime, timedelta, date
from pathlib import Path

from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

class BigQuery:
    def __init__(self):
        try:
            creds_file = './creds/gcp-service-account-key.json'
            credentials = service_account.Credentials.from_service_account_file(
                creds_file, 
                scopes=[
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/drive",
                    "https://www.googleapis.com/auth/bigquery",
                ]
            )
            self.client = bigquery.Client(credentials=credentials, project=credentials.project_id)

        except Exception as e:

            raise Exception(e)
    
    def query(self, query) -> pd.DataFrame:
        try:
            
            dataframe = self.client.query(query).to_dataframe()

            return dataframe
        except Exception as e:

            raise Exception(e)


def bq_to_bq_transfer(query: str, data_set: str, table_name: str, write_disposition: str,
                      time_partition_field: str) -> str:
    try:
        bigquery_client = create_bq_client()
        table_ref = bigquery_client.dataset(data_set).table(table_name)
        job_config = bigquery.QueryJobConfig(
            allow_large_results=True, destination=table_ref, use_legacy_sql=False)
        # partition control
        if time_partition_field != 'None':
            job_config.time_partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY,
                field=time_partition_field,
                expiration_ms=None)
        # append control
        if write_disposition == "Append":
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        else:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

        query_job = bigquery_client.query(query, job_config=job_config)
        query_job.result()

        return 'Completed'
    except Exception as e:

        raise Exception(e)


def bq_transfer_dataframe(data: pd.DataFrame, table_name: str, data_set: str, write_disposition: str) -> str:
    try:
        bigquery_client = create_bq_client()
        job_config = bigquery.LoadJobConfig()
        job_config.ignore_unknown_values = True
        job_config.allow_quoted_newlines = True
        job_config.autodetect = True
        job_config.allow_jagged_rows = True
        if write_disposition == "Append":
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        else:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

        table_ref = bigquery_client.dataset(data_set).table(table_name)
        job = bigquery_client.load_table_from_dataframe(
            data, table_ref, job_config=job_config)
        job.result()

        return 'Completed'
    except Exception as e:

        raise Exception(e)





def run_bigquery(query_bigquery) -> str:
    bigquery_client = create_bq_client()
    job = bigquery_client.query(query_bigquery)
    job.result()
    return 'Completed'

def get_days_ago_ga(day: int) -> str:
    from_date = str(datetime.strftime(date.today() - timedelta(days=day), "%Y%m%d"))

    return from_date


def get_days_ago(day: int) -> str:
    from_date = str(datetime.strftime(date.today() - timedelta(days=day), "%Y-%m-%d"))

    return from_date

def get_dates_since_ga(num_days_ago: int) -> str:
    dates = []
    for num_days in range(num_days_ago, 0, -1):
        dates.append(get_days_ago_ga(num_days))
    return dates