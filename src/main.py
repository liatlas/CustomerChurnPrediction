from data import main as download_data
from exploration import main as explore_data
from modeling import main as train_models
from wrangling import main as wrangle_data


def main():

    print("=" * 60)
    print("Downloading data")
    print("=" * 60)
    download_data()

    print("=" * 60)
    print("Cleaning data")
    print("=" * 60)
    wrangle_data()

    print("=" * 60)
    print("Generating EDA")
    print("=" * 60)
    explore_data()

    print("=" * 60)
    print("Training models")
    print("=" * 60)
    train_models()

    print("=" * 60)
    print("Pipeline complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
