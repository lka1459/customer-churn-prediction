import sys
import pandas as pd

from typing import List, Dict,TypedDict
from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats as stats

from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

class ModelConfig(TypedDict):
    model: XGBClassifier | LGBMClassifier
    param_grid: Dict[int, float]

def model_selection() -> ModelConfig:
    """
    Allows the user to select a model for training and returns both the model and the corresponding hyperparameter grid.
    """
    # While loop ensures that the user can only select one of the two models or exit the program
    while True:
        print("\nSelect a model: \n [1] XGB Booster \n [2] LGBM Classifier \n  \n [3] Exit \n")
        userInput: str = input("Enter choice: ")

        # XGB Booster and corresponding hyperparameter grid
        if userInput == "1":
            chosen_model: XGBClassifier =  XGBClassifier(n_estimators=100,
                                                        learning_rate=0.1,
                                                        max_depth=5,
                                                        random_state=42)
            param: Dict[int, float] = {
    'classifier__max_depth': stats.randint(3, 10),
    'classifier__learning_rate': stats.uniform(0.01, 0.1),
    'classifier__subsample': stats.uniform(0.5, 0.5),
    'classifier__n_estimators':stats.randint(50, 200)
                                }
            
            return chosen_model, param
       
       # LGBM Classifier and corresponding hyperparameter grid
        elif userInput == "2":
            chosen_model: LGBMClassifier = LGBMClassifier(random_state=42, verbose=-1)
            param: Dict[int, float] = {
    'classifier__learning_rate': stats.uniform(0.01, 0.2),
    'classifier__n_estimators': stats.randint(50, 200),
    'classifier__num_leaves': [15, 31, 63],
    'classifier__max_depth': stats.randint(3, 8)
                    }
            
            return chosen_model, param
        
        # Exit the program
        elif userInput == "3":
            sys.exit()
        
        # Error message
        else:
            print("\nInvalid choice, please try again.")

def fit_model(chosen_model: XGBClassifier | LGBMClassifier,
              param : Dict[str, float],
              preprocessor: ColumnTransformer, 
              X_train: pd.DataFrame, 
              y_train: pd.Series) -> RandomizedSearchCV:
    """
    Fits the model using RandomizedSearchCV and returns the trained model.
    """
    print("\nModel Training")
    print("=" * 30)
    
    # Defines the pipeline that combines the preprocessor and the model
    pipeline: Pipeline= Pipeline([
         ('preprocessor', preprocessor),
        ('classifier', chosen_model)
    ])

    # Creates a RandomizedSearchCV object with the specified model, hyperparameter grid, and cross-validation settings, and fits it to the training data
    rs: RandomizedSearchCV = RandomizedSearchCV(estimator=pipeline, param_distributions=param,  cv=5, scoring='accuracy', n_jobs=1, verbose=1)

    print("\nWaiting for model to train...")

    # Fitting the RandomizedSearchCV object to the training data
    trained_model: RandomizedSearchCV = rs.fit(X_train, y_train)

    print("\nModel finished training!")

    return trained_model

