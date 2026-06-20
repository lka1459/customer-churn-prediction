from typing import List, Tuple
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

def handleInStorePurchases(value) -> int:
    """
    Helper function used to deal with the null values.
    """
    if pd.isna(value):
        return 0
    else:
        return value

def data_preprocessing(olist_df) -> pd.DataFrame:
    """
    Applies all data cleaning/prepocessing necessary on the dataset.
    """
    olist_df['avg_delivery_lateness'] = olist_df['avg_delivery_lateness'].apply(handleInStorePurchases)

    olist_df["first_order_date"] = pd.to_datetime(olist_df["first_order_date"], format="%Y-%m-%d %H:%M:%S")
    olist_df["last_order_date"] = pd.to_datetime(olist_df["last_order_date"], format="%Y-%m-%d %H:%M:%S")

    reference_date: pd.Timestamp = olist_df["last_order_date"].max()
    olist_df['churn'] = np.where((reference_date - olist_df["last_order_date"]).dt.days > 180, 1, 0)
    return olist_df

def load_and_split(df) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    X: pd.DataFrame = df.drop(columns=["churn", "customer_unique_id"])
    y: pd.Series = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def build_preprocessor(X_train) -> ColumnTransformer:
    categorical_cols: List[str | object] = X_train.select_dtypes(include=["object", "string"]).columns.tolist()
    numerical_cols: List[int | float] = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()

    preprocessor: ColumnTransformer = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=True), categorical_cols)
        ]
    )

    return preprocessor