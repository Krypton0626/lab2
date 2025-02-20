import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def train_model(df):
    """Train a Random Forest model on the dataset."""
    df = df.copy()  # Avoid modification warnings

    # Drop non-numeric columns
    df.drop(columns=["id", "product_id"], inplace=True, errors="ignore")

    # Check for remaining non-numeric columns
    non_numeric = df.select_dtypes(include=['object']).columns
    if len(non_numeric) > 0:
        print(f"❌ Warning: Non-numeric columns found: {list(non_numeric)}. Ensure all are encoded or removed.")
        return

    X = df.drop(columns=["price"])
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"✅ Model MAE: {mae}")

if __name__ == "__main__":
    df = pd.read_csv("data/cab_rides.csv")
    train_model(df)