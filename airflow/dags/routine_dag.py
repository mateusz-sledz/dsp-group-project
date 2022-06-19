import sys
from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today

sys.path.append(".")
from backend.winequality.pipeline import load_pipeline_data, run_model_background


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

    df = get_data_for_pipeline()
    prediction = make_prediction_on_pipeline_data(df)
    return prediction


make_predictions = make_prediction_dag()
