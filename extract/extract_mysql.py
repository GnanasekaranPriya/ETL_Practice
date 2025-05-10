import pandas as pd
import mysql.connector
from config.db_config import MYSQL_CONFIG

def extract_orders():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    query = "SELECT * FROM orders"
    df = pd.read_sql(query, con=conn)
    conn.close()
    return df
