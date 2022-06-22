import os
import numpy as np
from dotenv import load_dotenv
# import joblib
import pandas as pd
import sklearn.metrics as metrics
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def build_model(data: pd.DataFrame) -> dict[str, float]:
    if os.getenv('ROOT') is None:
        load_dotenv()

    mlflow_user = os.getenv('DB_USER')
    mlflow_psw = os.getenv('DB_PSW')
    artifact = os.getenv('ROOT') + '/mlruns'

    tracking_uri = f"postgresql://{mlflow_user}:{mlflow_psw}@127.0.0.1:5432/winedb"
    mlflow.set_tracking_uri(tracking_uri)
    experiment_name = 'RandomForests_model'

    if not mlflow.get_experiment_by_name(experiment_name):
        mlflow.create_experiment(name=experiment_name, artifact_location=artifact)
    experiment = mlflow.get_experiment_by_name(experiment_name)

    with mlflow.start_run(experiment_id=experiment.experiment_id, run_name=f"run_{experiment_name}"):
        rand_state = np.random.randint(1, 100)

        Y_train = data['quality']
        X_train, X_test, y_train, y_test = \
            train_test_split(data.drop(['quality'], axis=1), Y_train, test_size=0.4, random_state=rand_state)

        model = RandomForestClassifier(random_state=rand_state)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        test_metrics = {
            'accuracy': metrics.accuracy_score(y_test, y_pred),
            'precision': metrics.precision_score(y_test, y_pred, average='micro'),
            'recall': metrics.recall_score(y_test, y_pred, average='micro'),
            'f-score': metrics.f1_score(y_test, y_pred, average='micro')
        }

        params = model.get_params()
        print(model.get_params())

        mlflow.sklearn.log_model(model, 'random forest classifier')
        mlflow.log_params(params)
        mlflow.log_metrics(test_metrics)

    return test_metrics
