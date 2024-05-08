# PostgreSQL Docker
1. Create folder Assignment-Docker
2. Download the dataset from kaggle https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
3. Create docker-compose.yml file
4. docker-compose.yml Code:
```
version: '3.8'
services:
  postgres-msib:
    image: postgres:15
    container_name: postgres-msib
    env_file:
      - .env
    volumes:
      - /var/lib/postgresql/data
    ports:
      - 5436:5432/tcp
```
4. Create .env file with this code:
```
POSTGRES_PASSWORD = postgres
POSTGRES_USER = postgres
POSTGRES_DB = postgres
POSTGRES_HOST_AUTH_METHOD=trust
```
5. Run docker with the command "docker compose up"
6. Create a connection with Postgresql, you can use the mysql extension in vs code

### Python Code
requirement module
- sqlalchemy

Code to Install:
!pip install sqlalchemy

7. Create etl.py with this code:
```
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
```
8. Create Dockerfile with the code:
```
# Use Python 3.9 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy etl.py into the container
COPY etl.py .

# Run the Python script
CMD ["python", "etl.py"]
```
