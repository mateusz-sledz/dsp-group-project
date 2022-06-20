import sys
from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today

sys.path.append(".")
from backend.winequality.pipeline import get_data_for_retraining, retrain_model


@dag(
    dag_id="retrain_45_sec",
    description="Retrain model every 35 seconds",
    schedule_interval=timedelta(seconds=45),
    start_date=today(),
    catchup=False,
    tags=["retrain_model"],   
)
def retrain_dag():
    @task
    def get_retraining_data():
        return get_data_for_retraining()

    @task
    def retrain(data_df):
        return retrain_model(data_df)

    df = get_retraining_data()
    return retrain(df)


retrain = retrain_dag()
