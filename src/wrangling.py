import pandas as pd

def load() -> pd.DataFrame:
    return pd.read_csv("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

def remove_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the customerID column from removes_columns.
    """

def convert_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts all columns to snake_case
    """

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

def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the 11 missing values from total_charges
    """

def convert_float_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts total_id column to type float
    """

def save_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Save the final df to "../data/clean/dataset.csv" with no index
    """
