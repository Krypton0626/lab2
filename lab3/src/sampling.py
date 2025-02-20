import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

def check_numeric_column(df, column):
    """Check if the column is numeric and handle non-numeric values."""
    if df[column].dtype == 'object':
        df[column] = pd.to_numeric(df[column], errors='coerce')
    df = df.dropna(subset=[column])
    return df

def stratified_sampling(df, target_col, test_size=0.2):
    """Perform stratified sampling by binning the target variable."""
    df = check_numeric_column(df, target_col)
    
    if df[target_col].value_counts().min() < 2:
        return random_sampling(df, test_size)

    try:
        sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=42)
        for train_index, test_index in sss.split(df, df[target_col]):
            train_set = df.iloc[train_index]
            test_set = df.iloc[test_index]
        return train_set, test_set
    except:
        return random_sampling(df, test_size)

def random_sampling(df, test_size=0.2):
    """Perform random sampling."""
    df = check_numeric_column(df, "price")
    train_size = 1 - test_size
    train_set = df.sample(frac=train_size, random_state=42)
    test_set = df[~df.index.isin(train_set.index)]
    return train_set, test_set

def cluster_sampling(df, cluster_col, test_size=0.2):
    """Perform cluster sampling."""
    df = check_numeric_column(df, "price")
    try:
        clusters = df[cluster_col].unique()
        np.random.seed(42)
        selected_clusters = np.random.choice(
            clusters, 
            size=int(len(clusters) * (1 - test_size)), 
            replace=False
        )
        train_set = df[df[cluster_col].isin(selected_clusters)]
        test_set = df[~df[cluster_col].isin(selected_clusters)]
        return train_set, test_set
    except:
        return random_sampling(df, test_size)

def systematic_sampling(df, test_size=0.2):
    """Perform systematic sampling."""
    df = check_numeric_column(df, "price")
    try:
        n = len(df)
        k = int(1 / (1 - test_size))
        indices = np.arange(0, n, k)
        train_set = df.iloc[indices]
        test_set = df.drop(train_set.index)
        return train_set, test_set
    except:
        return random_sampling(df, test_size)