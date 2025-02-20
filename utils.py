import pandas as pd

def load_clean_data(filepath):
    """Loads and preprocesses dataset."""
    df = pd.read_csv(filepath)
    df.drop_duplicates(inplace=True)
    return df