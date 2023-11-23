from pathlib import Path

from fastapi import FastAPI
import pandas as pd

from src.utils.bigquery import BigQuery

app = FastAPI()
bq = BigQuery()

@app.get("/")
async def get_pct_ingresos_sobre_gasto():
    pct_ingresos_sobre_gasto_query_file = Path('sql/pct_ingresos_sobre_gasto.sql')
    df = bq.query(pct_ingresos_sobre_gasto_query_file.read_text())
    return df.to_dict()