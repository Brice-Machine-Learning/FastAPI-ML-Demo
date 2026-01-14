from sklearn.datasets import fetch_california_housing
from pathlib import Path

def create_dataset():
    data = fetch_california_housing(as_frame=True)
    df = data.frame

    Path("data").mkdir(exist_ok=True)
    df.to_csv("../data/raw/california_housing.csv", index=False)

    print("Dataset written to data/california_housing.csv")

if __name__ == "__main__":
    create_dataset()
