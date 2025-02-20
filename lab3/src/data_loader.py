import pandas as pd

def load_data(cab_rides_path, weather_path):
    """Loads and merges cab rides & weather data."""
    # Load datasets
    cab_rides = pd.read_csv(cab_rides_path)
    weather = pd.read_csv(weather_path)

    # Merge on location and timestamp
    merged_df = cab_rides.merge(weather, left_on=["source", "time_stamp"], right_on=["location", "time_stamp"], how="left")

    # Drop redundant columns
    merged_df.drop(columns=["location"], inplace=True)

    return merged_df