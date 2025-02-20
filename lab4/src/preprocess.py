import pandas as pd
from sklearn.preprocessing import StandardScaler

def handle_missing_values(df):
    """Fill missing values in dataset."""
    df.fillna({'price': df['price'].median(), 'surge_multiplier': 1.0}, inplace=True)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df

def encode_features(df):
    """Apply one-hot encoding to categorical variables."""
    categorical_cols = ["cab_type", "name", "source", "destination"]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def scale_features(df, feature_cols):
    """Standardize numerical features."""
    scaler = StandardScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/cab_rides.csv")
    df = handle_missing_values(df)
    df = encode_features(df)
    print(df.head())