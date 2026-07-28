import numpy as np
import pandas as pd


# Helper Functions
def to_snake_case(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')

# Main Steps

def load() -> pd.DataFrame:
    return pd.read_csv("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

def remove_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the customerID column from removes_columns.
    """

    df_copy = df.copy()

    df_copy = df_copy.drop("customerID", axis=1)

    return df_copy

def convert_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts all columns to snake_case
    """
    df_copy = df.copy()

    df_copy.columns = [to_snake_case(c) for c in df_copy.columns]

    df_copy = df_copy.rename(columns={"streaming_t_v": "streaming_tv"})

    return df_copy

def convert_bool_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts columns:
        * churn 
        * phone_service
        * dependents
        * partner 
        * paperless_billing
    to bool, because they are yes, no columns
    """
    bool_columns = ["churn", "phone_service", "dependents", "partner", "paperless_billing"]
    
    df_copy = df.copy()

    for col in bool_columns:
        df_copy[col] = pd.Series(np.where(df_copy[col].values == 'Yes', 1, 0), df_copy.index)

    return df_copy

def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the 11 missing values from total_charges
    """

    df_copy = df.copy()

    df_copy = df_copy.drop(
        df_copy[df_copy.total_charges == ' '].index
    )

    return df_copy

def convert_float_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts total_id column to type float
    """
    df_copy = df.copy()

    df_copy['total_charges'] = df_copy['total_charges'].astype('float')

    return df_copy

def save_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Save the final df to "../data/clean/dataset.csv" with no index
    """
    df.to_csv("../data/clean/dataset.csv", index=False)

def main():
    df = (
        load()
        .pipe(remove_columns)
        .pipe(convert_column_names)
        .pipe(convert_bool_types)
        .pipe(remove_missing_values)
        .pipe(convert_float_types)
    )

    save_df(df)
    print("Saved cleaned dataset.")

if __name__ == "__main__":
    main()
