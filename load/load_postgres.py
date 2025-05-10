from sqlalchemy import create_engine
from config.db_config import POSTGRES_URI

def load_to_postgres(df, table_name):
    engine = create_engine(POSTGRES_URI)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
