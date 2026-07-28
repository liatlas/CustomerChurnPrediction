from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

MODEL_DIR = Path("../outputs/models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def load():
    return pd.read_csv("../data/clean/dataset.csv")


def split(df):
    X = df.drop("churn", axis=1)
    X = pd.get_dummies(X, drop_first=True)

    y = df["churn"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )


def preprocess(X_train, X_test, y_train):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    selector = SelectKBest(
        score_func=mutual_info_classif,
        k=10,
    )

    X_train_best = selector.fit_transform(
        X_train_scaled,
        y_train,
    )

    X_test_best = selector.transform(
        X_test_scaled,
    )

    return (
        X_train_best,
        X_test_best,
        scaler,
        selector,
    )


def evaluate(model, X_test, y_test):

    preds = model.predict(X_test)

    print("=" * 40)
    print(model.__class__.__name__)
    print("=" * 40)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))


def train_models(
    X_train,
    X_test,
    y_train,
    y_test,
):

    models = {
        "logistic_regression": LogisticRegression(max_iter=5000),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            random_state=42,
        ),
        "gradient_boosting": GradientBoostingClassifier(
            random_state=42,
        ),
        "svm": SVC(
            kernel="rbf",
            probability=True,
        ),
    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        evaluate(model, X_test, y_test)

        joblib.dump(
            model,
            MODEL_DIR / f"{name}.joblib",
        )


def main():

    df = load()

    (
        X_train,
        X_test,
        y_train,
        y_test,
    ) = split(df)

    (
        X_train,
        X_test,
        scaler,
        selector,
    ) = preprocess(
        X_train,
        X_test,
        y_train,
    )

    train_models(
        X_train,
        X_test,
        y_train,
        y_test,
    )

    joblib.dump(
        scaler,
        MODEL_DIR / "scaler.joblib",
    )

    joblib.dump(
        selector,
        MODEL_DIR / "selector.joblib",
    )


if __name__ == "__main__":
    main()
