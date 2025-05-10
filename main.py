from extract.extract_mysql import extract_orders
from transform.transform_data import clean_orders
from load.load_postgres import load_to_postgres

def run_etl():
    print("Extracting...")
    raw_df = extract_orders()
    print("Transforming...")
    clean_df = clean_orders(raw_df)
    print("Loading...")
    load_to_postgres(clean_df, 'clean_orders')
    print("ETL Completed.")



if __name__ == '__main__':
    run_etl()