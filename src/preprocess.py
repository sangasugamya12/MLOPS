import pandas as pd
import os


def clean_data():
    df = pd.read_csv("data/raw/students.csv")
    df.dropna(inplace=True)

    # Convert gender
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Save
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Data cleaned and saved at data/processed/cleaned.csv")
    return df


def load_and_clean():
    df = pd.read_csv("data/raw/students.csv")
    df = df.dropna()
    df = pd.get_dummies(df, drop_first=True)

    # Make sure this folder exists before saving
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Data cleaned and saved at data/processed/cleaned.csv")


# This line ensures the function runs when the script is executed directly
if __name__ == "__main__":
    load_and_clean()