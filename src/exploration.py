from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

OUTPUT_DIR = Path("../outputs/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load():
    return pd.read_csv("../data/clean/dataset.csv")


def save_figure(fig, filename):
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=150)
    plt.close(fig)


def save_churn(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.countplot(data=df, x="churn", ax=ax)

    ax.set_title("Counts of Churn")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Count")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["No", "Yes"])

    save_figure(fig, "churn_distribution.png")


def save_tenure_by_churn(df):
    fig, ax = plt.subplots(figsize=(6, 4))

    sns.histplot(
        data=df,
        x="tenure",
        hue="churn",
        kde=True,
        multiple="stack",
        palette="Set2",
        ax=ax,
    )

    ax.set_title("Tenure Distribution by Churn")
    ax.set_xlabel("Tenure (months)")

    save_figure(fig, "tenure_by_churn.png")


def save_monthly_charges_by_churn(df):
    fig, ax = plt.subplots(figsize=(6, 4))

    sns.histplot(
        data=df,
        x="monthly_charges",
        hue="churn",
        kde=True,
        multiple="stack",
        palette="Set2",
        ax=ax,
    )

    ax.set_title("Monthly Charges Distribution by Churn")
    ax.set_xlabel("Monthly Charges ($)")

    save_figure(fig, "monthly_charges_by_churn.png")


def save_total_charges_by_churn(df):
    fig, ax = plt.subplots(figsize=(5, 4))

    sns.boxplot(
        data=df,
        x="churn",
        y="total_charges",
        hue="churn",
        palette="Set2",
        legend=False,
        ax=ax,
    )

    ax.set_title("Total Charges by Churn")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Total Charges ($)")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["No", "Yes"])

    save_figure(fig, "total_charges_by_churn.png")


def save_tenure_vs_monthly_charges(df):
    fig, ax = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=df,
        x="tenure",
        y="monthly_charges",
        hue="churn",
        alpha=0.6,
        ax=ax,
    )

    ax.set_title("Tenure vs Monthly Charges (colored by Churn)")
    ax.set_xlabel("Tenure (months)")
    ax.set_ylabel("Monthly Charges ($)")

    save_figure(fig, "tenure_vs_monthly_charges.png")


def save_tenure_by_total_charges(df):
    fig, ax = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=df,
        x="tenure",
        y="total_charges",
        hue="churn",
        alpha=0.6,
        ax=ax,
    )

    ax.set_title("Tenure vs Total Charges (colored by Churn)")
    ax.set_xlabel("Tenure (months)")
    ax.set_ylabel("Total Charges ($)")

    save_figure(fig, "tenure_vs_total_charges.png")


def save_heatmap(df):
    numeric_cols = [
        "senior_citizen",
        "partner",
        "dependents",
        "tenure",
        "paperless_billing",
        "monthly_charges",
        "total_charges",
        "churn",
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax,
    )

    ax.set_title("Correlation Heatmap")

    save_figure(fig, "heatmap.png")


def save_categorical_plots(df):
    categorical_cols = [
        "contract",
        "internet_service",
        "payment_method",
        "tech_support",
        "online_security",
        "online_backup",
        "device_protection",
        "senior_citizen",
        "partner",
        "dependents",
        "gender",
    ]

    for col in categorical_cols:
        fig, ax = plt.subplots(figsize=(6, 4))

        sns.countplot(data=df, x=col, hue="churn", ax=ax)

        ax.set_title(f"Churn by {col.replace('_', ' ').title()}")
        ax.set_xlabel(col.replace("_", " ").title())
        ax.set_ylabel("Number of Customers")

        for label in ax.get_xticklabels():
            label.set_rotation(30)
            label.set_ha("right")

        ax.legend(title="Churn")

        save_figure(fig, f"{col}_churn.png")


def main():
    df = load()

    save_churn(df)
    save_tenure_by_churn(df)
    save_monthly_charges_by_churn(df)
    save_total_charges_by_churn(df)
    save_tenure_vs_monthly_charges(df)
    save_tenure_by_total_charges(df)
    save_heatmap(df)
    save_categorical_plots(df)


if __name__ == "__main__":
    main()
