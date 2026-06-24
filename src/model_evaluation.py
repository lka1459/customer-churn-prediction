import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, RocCurveDisplay, PrecisionRecallDisplay


def evaluate_model(final_model: RandomizedSearchCV, X_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Evaluates the performance of the trained model using a classification report, confusion matrix, precision-recall curve and ROC curve.
    The results are saved in the "results" folder.
    """
    # Ensuring that each relevant folder exists before saving the results
    Path("results/reports").mkdir(parents=True, exist_ok=True)
    Path("results/plots").mkdir(parents=True, exist_ok=True)
    
    # Extracting the best model from the RandomizedSearchCV object and creating y_pred using the test set
    model: Pipeline = final_model.best_estimator_
    y_pred: np.ndarray = model.predict(X_test)

    # Writes classification report and saves it to "results/reports/classification_report.txt"
    report: str = classification_report(y_test, y_pred)
    with open(r"results/reports/classification_report.txt", "w") as f:
        f.write(report)

    # Creates a confusion matrix and saves it to "results/reports/confusion_matrix.txt"
    matrix: np.ndarray = confusion_matrix(y_test, y_pred)
    cm: ConfusionMatrixDisplay = ConfusionMatrixDisplay(confusion_matrix=matrix)
    cm.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.savefig(r"results/plots/confusion_matrix.png")
    plt.close()

    # Creates a precision-recall curve and saves it to "results/plots/pr_chart.png"
    sns.set_theme(style="whitegrid")
    PrecisionRecallDisplay.from_estimator(model, X_test, y_test)
    plt.title("Precision-Recall (PR) Chart")
    plt.savefig(r"results/plots/pr_chart.png")  
    plt.close()

    # Creates a ROC curve and saves it to "results/plots/roc_curve.png"
    sns.set_theme(style="darkgrid")
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.title("ROC Curve Results")
    plt.savefig(r"results/plots/roc_curve.png")
    plt.close()