import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, RocCurveDisplay, PrecisionRecallDisplay


def evaluate_model(final_model, X_test, y_test):
    model: Pipeline = final_model.best_estimator_
    y_pred: np.ndarray = model.predict(X_test)
    report: str = classification_report(y_test, y_pred)
    with open(r"results/reports/classification_report.txt", "w") as f:
        f.write(report)

    matrix: np.ndarray = confusion_matrix(y_test, y_pred)
    cm: ConfusionMatrixDisplay = ConfusionMatrixDisplay(confusion_matrix=matrix)
    cm.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.savefig(r"results/plots/confusion_matrix.png")

    sns.set_theme(style="whitegrid")
    PrecisionRecallDisplay.from_estimator(model, X_test, y_test)
    plt.title("Precision-Recall (PR) Chart")
    plt.savefig(r"results/plots/pr_chart.png")  

    sns.set_theme(style="darkgrid")
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.title("ROC Curve Results")
    plt.savefig(r"results/plots/roc_curve.png")  