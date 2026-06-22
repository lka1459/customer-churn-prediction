import pandas as pd
import numpy as np

from typing import List, Dict
from sklearn.pipeline import Pipeline


def get_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer.")

def get_float(prompt) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid floating point number.")
        

def get_date(prompt) -> pd.to_datetime:
    while True:
        try:
            return pd.to_datetime(input(prompt), format="%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Please enter a date wi")

def churn_predictor(model: Pipeline) -> str:
    print("\nUser Prediction")
    print("=" * 30)

    avg_freight: float = get_float("avg_freight: ")
    total_spent: int = get_int("total_spent: ")
    average_spent: float = get_float("average_spent: ")
    avg_delivery_lateness: float = get_float("avg_delivery_lateness: ")
    first_order_date: pd.Timestamp = get_date("Enter the first order date (YYYY-MM-DD H:M:S): ")
    last_order_date: pd.Timestamp = get_date("Enter the last order date (YYYY-MM-DD H:M:S): ")
    total_orders: int = get_int("total_orders: ")
    avg_review_score: float = get_float("avg_review_score: ")
    num_categories: int = get_int("num_categories: ")

    data: Dict[List] = {
        "avg_freight": [avg_freight],
        "total_spent": [total_spent],
        "average_spent": [average_spent],
        "avg_delivery_lateness": [avg_delivery_lateness],
        "first_order_date": [first_order_date],
        "last_order_date": [last_order_date],
        "total_orders": [total_orders],
        "avg_review_score": [avg_review_score],
        "num_categories": [num_categories]
    }

    processed_input: pd.DataFrame = pd.DataFrame(data)

    final_prediction: np.ndarray = model.predict(processed_input)

    if final_prediction == 1:
        result: str = "\nPrediction Result: Customer will churn."
    else:
        result: str = "\nPrediction Result: Customer will not churn."

    return f"""
\nFinal Prediction
{"=" * 30}
{result}
    """


