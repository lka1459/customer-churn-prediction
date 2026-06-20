import sys
import pandas as pd

from typing import List, Dict
from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats as stats

from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

def model_selection() -> List[Dict]:
    while True:
        print("\nSelect a model: \n [1] XGB Booster \n [2] LGBM Classifier \n  \n [3] Exit \n")
        userInput: str = input("Enter choice: ")
        if userInput == "1":
            chosen_model: XGBClassifier =  XGBClassifier(n_estimators=100,
                                                        learning_rate=0.1,
                                                        max_depth=5,
                                                        random_state=42)
            param: List[Dict] = {
    'classifier__max_depth': stats.randint(3, 10),
    'classifier__learning_rate': stats.uniform(0.01, 0.1),
    'classifier__subsample': stats.uniform(0.5, 0.5),
    'classifier__n_estimators':stats.randint(50, 200)
                                }
            return chosen_model, param
        elif userInput == "2":
            chosen_model: LGBMClassifier = LGBMClassifier(random_state=42, verbose=-1)
            param = {
    'classifier__learning_rate': stats.uniform(0.01, 0.2),
    'classifier__n_estimators': stats.randint(50, 200),
    'classifier__num_leaves': [15, 31, 63],
    'classifier__max_depth': stats.randint(3, 8)
                    }
            return chosen_model, param
        elif userInput == "3":
            sys.exit()
        else:
            print("\nInvalid choice, please try again.")



def fit_model(chosen_model,
              param,
              preprocessor: ColumnTransformer, 
              X_train: pd.DataFrame, 
              y_train: pd.Series) -> Pipeline:
    
    print("Model Training")
    print("=" * 30)
    
    pipeline: Pipeline= Pipeline([
         ('preprocessor', preprocessor),
        ('classifier', chosen_model)
    ])


    rs = RandomizedSearchCV(estimator=pipeline, param_distributions=param,  cv=5, scoring='accuracy', n_jobs=1, verbose=1)

    print("\nWaiting for model to train...")

    trained_model: Pipeline = rs.fit(X_train, y_train)

    print("\nModel finished training!")

    return trained_model

