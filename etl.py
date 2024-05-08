import pandas as pd
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'postgres'
hostname  = '127.0.0.1'
database  = 'postgres'
port      = '5436'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

# ---------- Mengambil data dan jadiin Table di database------
df = pd.read_csv('supermarket_sales.csv')
df.to_sql("sales",engine, if_exists='replace')

# ---------- Mengambil tabel di database untuk Agregasi data ----------
query   = "SELECT Product_line, AVG(Unit_price) as harga_satuan_rata2 FROM sales"
df_read = pd.read_sql(query,engine)
df_read.to_sql("agregasi",engine, if_exists='replace')
df_read.head()