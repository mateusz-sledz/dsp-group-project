import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#def build_model(data: pd.DataFrame) -> dict[str, str]:


def build_model(data: pd.DataFrame):
    print(data.shape)
    Y_train = data['quality']
    X_train, X_test, y_train, y_test =\
        train_test_split(data.drop(['quality'], axis=1), Y_train, test_size=0.4,
                                                        random_state=30)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump('../models/RANDOM_FOREST_MODEL')

