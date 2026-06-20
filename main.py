import pandas as pd
from pathlib import Path


from src.database_setup import create_database, read_SQL_Query
from src.data_preprocessing import build_preprocessor, data_preprocessing, load_and_split

def initial_setup() -> pd.DataFrame:
    print("Customer Churn Prediction")
    print("=" * 30)

    file_path: Path = Path(r"database\olist.db")

    if not file_path.is_file():
        create_database()
    
    initial_df: pd.DataFrame = read_SQL_Query(r"sql\modeling\churn_features.sql")
    df: pd.DataFrame = data_preprocessing(initial_df)
    return df

def main():
    df = initial_setup()

    X_train, X_test, y_train, y_test = load_and_split(df)
    preprocessor = build_preprocessor(X_train)

if __name__ == "__main__":
    main()