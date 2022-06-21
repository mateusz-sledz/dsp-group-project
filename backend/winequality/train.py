import os
from dotenv import load_dotenv
import joblib
import pandas as pd
import sklearn.metrics as metrics
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def build_model(data: pd.DataFrame) -> dict[str, float]:
    Y_train = data['quality']
    X_train, X_test, y_train, y_test =\
        train_test_split(data.drop(['quality'], axis=1), Y_train, test_size=0.4)

    with mlflow.start_run():
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        if os.getenv('ROOT') is None:
            load_dotenv()

        joblib.dump(model, os.getenv('ROOT') + '/backend/models/RANDOM_FOREST_MODEL')

        y_pred = model.predict(X_test)

        test_metrics = {
            'accuracy': metrics.accuracy_score(y_test, y_pred),
            'precision': metrics.precision_score(y_test, y_pred, average='micro'),
            'recall': metrics.recall_score(y_test, y_pred, average='micro'),
            'f-score': metrics.f1_score(y_test, y_pred, average='micro')
        }

        print(model.get_params())
        experiment_name = "wine_prediction_with_random_forest"
        # mlflow.set_experiment(experiment_name)
        # mlflow.log_metrics(test_metrics)

    return test_metrics
