import pandas as pd
import warnings
from pathlib import Path

from sklearn.model_selection import RandomizedSearchCV
from sklearn.compose._column_transformer import ColumnTransformer

from src.database_setup import create_database, read_SQL_Query
from src.data_preprocessing import build_preprocessor, data_preprocessing, load_and_split
from src.model_pipeline import model_selection, fit_model
from src.model_evaluation import evaluate_model
from src.predictive_inference import churn_predictor

def initial_setup() -> pd.DataFrame:
    """
    Initial setup for the customer churn prediction project.
    """
    print("Customer Churn Prediction")
    print("=" * 30)

    # Confirming the existence of the database and creating it if it doesn't exist
    file_path: Path = Path(r"database\olist.db")

    if not file_path.is_file():
        create_database()
    
    # Load the initial dataset and applying preprocessing steps
    initial_df: pd.DataFrame = read_SQL_Query(r"sql\modeling\churn_features.sql")
    df: pd.DataFrame = data_preprocessing(initial_df)

    return df

def main() -> None:
    """
    Main function to run the customer churn prediction pipeline.
    """
    # Surpresses warning for cleaner output
    warnings.filterwarnings('ignore', category=UserWarning)

    # Initial setup: database creation, data loading and preprocessing    
    df: pd.DataFrame = initial_setup()

    # Splitting the dataset and building the preprocessor
    X_train, X_test, y_train, y_test = load_and_split(df)
    preprocessor: ColumnTransformer = build_preprocessor(X_train)

    # Selecting the model of choice and fitting it to the training data
    model, param_grid = model_selection()
    trained_model: RandomizedSearchCV = fit_model(model, param_grid,preprocessor, X_train, y_train)

    # Creating visualisations and reports of the model performance on the test set
    evaluate_model(trained_model, X_test, y_test)

    # Allows the user to input customer features and returns a churn prediction based on the trained model.
    print(churn_predictor(trained_model))

if __name__ == "__main__":
    main()