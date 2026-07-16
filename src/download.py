import kagglehub
from pathlib import Path

def verify_dir(dir):
    if not dir.is_dir():
        raise FileNotFoundError(f"{dir} was not created")

def verify_csv(file, dir):
    csv_path = dir / file

    if not csv_path.is_file():
        raise FileNotFoundError(f"Expected file not found: {csv_path}")

def download(output_dir=Path("./data/raw")):
    """
    Downloads the "blastchar/telco-customer-churn" dataset and saves it to ./data/raw
    """

    path = kagglehub.dataset_download(
        "blastchar/telco-customer-churn",

        output_dir="./data/raw"

    )

    verify_dir(output_dir)
    verify_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv", output_dir)

    print(f"Downloaded data to {path}")

if __name__ == "__main__":
    download()
