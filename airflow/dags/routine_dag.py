import sys
sys.path.append("..")
sys.path.append(".")

from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
from backend.winequality.pipeline import load_pipeline_data, run_model_background


@dag(
    dag_id="first_injection",
    description="data injection for testing",
    schedule_interval=timedelta(seconds=10),
    start_date=today().add(hours=-1),
    tags=["first_injection"],
)
def make_prediction_dag():
    # Define tasks
    @task
    def get_data_for_pipeline():
        return load_pipeline_data()
#           return [1,2,3]

    @task
    def make_prediction_on_pipeline_data(data_df):
        return run_model_background(data_df)

    df = get_data_for_pipeline()
    prediction = make_prediction_on_pipeline_data(df)
#     return [1,2,3]
    return prediction


make_predictions = make_prediction_dag()
#
# #
# def load_pipeline_data():
#     data = load_pipeline_data()
#     data = [1,2,3]
# #     data = pd.read_csv('/Users/meghas/EPITA/S2/gitandVersioning/dsp-group-project/backend/data/injection_data1.csv')
#     return data
# #
# #
# def run_model_background(data):
#     df_copy = data.copy()
#     model = joblib.load('/Users/meghas/EPITA/S2/gitandVersioning/dsp-group-project/backend/models/RANDOM_FOREST_MODEL')
#     return data
