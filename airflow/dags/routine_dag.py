import sys
from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
import logging

sys.path.append(".")
from backend.winequality.pipeline import load_pipeline_data, run_model_background
from backend.postgres_handler.connector import save_to_db


@dag(
    dag_id="predict_every_30_seconds",
    description="Perdict an instance of data every 30 seconds",
    schedule_interval=timedelta(seconds=30),
    start_date=today(),
    catchup=False,
    tags=["prediction"],
)
def make_prediction_dag():
    @task
    def get_data_for_pipeline():
        return load_pipeline_data()

    @task
    def make_prediction_on_pipeline_data(data_df):
        return run_model_background(data_df)

    @task
    def send_data_to_postgres(values, pred):
        data = values[0].tolist()
        data.append(float(pred[0]))
        save_to_db([data])
        logging.info('SENT TO DB')

    df = get_data_for_pipeline()
    prediction = make_prediction_on_pipeline_data(df)
    send_data_to_postgres(df, prediction)

    return prediction


make_predictions = make_prediction_dag()
