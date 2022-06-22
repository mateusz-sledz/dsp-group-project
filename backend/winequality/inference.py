import os
from dotenv import load_dotenv
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient


def make_predictions(data: pd.DataFrame) -> dict[str, str]:
    client = MlflowClient()
    if os.getenv('ROOT') is None:
        load_dotenv()

    experiment_name = 'RandomForests_model'
    experiment_id = client.get_experiment_by_name(experiment_name).experiment_id

    all_runs_info = client.list_run_infos(experiment_id)
    all_runs_id = [run.run_id for run in all_runs_info]
    all_params = [client.get_run(run_id).data.params['random_state'] for run_id in all_runs_id]
    all_metrics = [client.get_run(run_id).data.metrics['accuracy'] for run_id in all_runs_id]

    df = pd.DataFrame({'id': all_runs_id, 'params': all_params, 'metrics': all_metrics})

    best_run_id = df.sort_values('metrics', ascending=False).iloc[0]['id']
    best_model_path = client.download_artifacts(best_run_id, 'random forest classifier')
    print('using model:', best_model_path, 'with id:', best_run_id)
    best_model = mlflow.sklearn.load_model(best_model_path)

    df_copy = data.copy()
    return best_model.predict(df_copy)
