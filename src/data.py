import kagglehub
from pathlib import Path
import shutil


DATA_DIR = Path("../data/raw")


def download(dataset):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    path = kagglehub.dataset_download(dataset)

    print(f"Downloaded dataset: {path}")

    # Copy files into project data directory
    src = Path(path)

    for file in src.iterdir():
        dest = DATA_DIR / file.name

        if file.is_file():
            shutil.copy2(file, dest)
        elif file.is_dir():
            shutil.copytree(file, dest, dirs_exist_ok=True)

    print(f"Saved dataset to: {DATA_DIR}")


def main():
    dataset = "blastchar/telco-customer-churn"  # replace
    download(dataset)


if __name__ == "__main__":
    main()

