from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.operators.dummy_operator import DummyOperator



file_path='/home/jed/blossom/dags/data/dvd/'
dataset='staging'

default_args = {
    'owner': 'jed',
    'depends_on_past': True,
    'start_date': datetime(2019, 12, 10),
    'email': ['jmadjanor6@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}



with DAG(dag_id='warehouse', schedule_interval=timedelta(days=1), default_args=default_args) as dag:
    
    start_staging = DummyOperator(
        task_id='start_staging'

    )
    end_staging = DummyOperator(
        task_id='end_staging'
    )



    tabl = {
        'actors':'actor.csv',
        'address':'address.csv',
        'categories':'category.csv',
        'cities':'city.csv',
        'countries':'country.csv',
        'customers':'customer.csv',
        'films':'film.csv',
        'film_actors':'film_actor.csv',
        'film_categories':'film_category.csv',
        'inventories':'inventory.csv',
        '_languages_':'_language_.csv',
        'payments':'payment.csv',
        'rentals':'rental.csv',
        'staffs':'staff.csv',
        'stores':'store.csv'
    }


    for tab, fal in tabl.items():
        tab = BashOperator(
            task_id=f'extract_{tab}',
            bash_command=f'bq load --autodetect {dataset}.{tab} {file_path}{fal}'
        )
        start_staging>>tab>>end_staging


    dim_customer = BigQueryOperator(
        task_id='dim_customer',
        sql='sql/dimensions/dim_customer.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.dim_customer',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )


    dim_film = BigQueryOperator(
        task_id='dim_film',
        sql='sql/dimensions/dim_film.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.dim_film',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )


    dim_store = BigQueryOperator(
        task_id='dim_store',
        sql='sql/dimensions/dim_store.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.dim_store',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )


    fact_sales = BigQueryOperator(
        task_id='fact_sales',
        sql='sql/facts/dim_store.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.fact_sales',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )

    fact_customer_count = BigQueryOperator(
        task_id='fact_customer_count',
        sql='sql/facts/fact_customer_count.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.fact_customer_count',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )

    fact_rental_count = BigQueryOperator(
        task_id='fact_rental_count',
        sql='sql/facts/fact_rental_count.sql ',
        use_legacy_sql=False,
        destination_dataset_table='databig-260523.warehouse.fact_rental_count',
        bigquery_conn_id='my_bq',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )


    end_warehouse = DummyOperator(
        task_id='end_warehouse'
    )

    end_fact = DummyOperator(
        task_id='end_fact'
    )


    end_staging>>[dim_customer, dim_store, dim_film]>>end_warehouse
    end_warehouse>>[fact_sales, fact_customer_count, fact_rental_count]>>end_fact